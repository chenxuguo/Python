import asyncio
import functools
import inspect
import time
from typing import Awaitable, Callable, Final, overload, ParamSpec, Protocol, TypeVar


async def print_with_timer(format: str, interval: float = 0.1) -> None:
    start = time.time()
    while True:
        elapsed = time.time() - start
        print(format.format(elapsed=elapsed), end="")
        await asyncio.sleep(interval)


OVERWRITE_LINE: Final[str] = "\033[F"
TIMER_FORMAT: Final[str] = f"\n{OVERWRITE_LINE}Invocation {{module}}.{{name}}({{arguments}}) has been running for {{{{elapsed:0.2f}}}}s"


P = ParamSpec("P")
R = TypeVar("R")

class Decorator(Protocol):
    def __call__(self, func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
        ...


@overload
def with_timer(interval_or_callback: float) -> Decorator:
    ...

@overload
def with_timer(interval_or_callback: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
    ...

def with_timer(interval_or_callback: float | Callable[P, Awaitable[R]]) -> Decorator | Callable[P, Awaitable[R]]:
    def inner(func: Callable[P, Awaitable[R]]) -> Callable[P, Awaitable[R]]:
        @functools.wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            arguments = inspect.signature(func).bind(*args, **kwargs).arguments
            argument_string = ", ".join(f"{name} = {value!r}" for name, value in arguments.items())
            timer_format = TIMER_FORMAT.format(module=func.__module__, name=func.__qualname__, arguments=argument_string)
            if isinstance(interval_or_callback, float):
                task = asyncio.create_task(print_with_timer(timer_format, interval_or_callback))
            else:
                task = asyncio.create_task(print_with_timer(timer_format))
            try:
                result = await func(*args, **kwargs)
            finally:
                task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            print()
            return result
        return wrapper

    if isinstance(interval_or_callback, float):
        return inner

    return inner(interval_or_callback)


@with_timer
async def do_stuff() -> int:
    await asyncio.sleep(5.0)
    return 42


@with_timer(0.5)
async def do_more_stuff(duration: float) -> str:
    await asyncio.sleep(duration)
    return "Do a good turn daily."

reveal_type(do_stuff)
reveal_type(do_more_stuff)

async def main() -> int:
    important_number = await do_stuff()
    print(f"The meaning of life is {important_number}")
    scout_slogan = await do_more_stuff(3.0)
    print(f"The scout slogan is \"{scout_slogan}\"")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))