from typing import TypeVar, Protocol

Self = TypeVar("Self", bound="Addable")

class Addable(Protocol):
    def __add__(self:Self, other:Self) -> Self:
        ...

T = TypeVar("T", bound=Addable)

def add(x: T, y:T) -> T:
	return x + y
	

print(add("foo", "bar"))