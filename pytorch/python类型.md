[type](https://samgeo.codes/blog/python-types/)
Guido van Rossum and Ivan Levkivskyi created PEP 483 proposing a type hinting system for Python.

I'll be using mypy since it seems to be the most widely used tool, at the moment.

    def add(x, y):
		return x + y

	print(add(1, 2))

Let's modify our program
    def add(x: int, y: int) -> int:
		return x + y

	print(add(1, 2))

But a lot of the power of using python comes from being able to use functions in a flexible manner.

    from typing import TypeVar

	T = TypeVar('T')

	def add(x: T, y: T) -> T:
		return x + y

	print(add("foo", "bar"))


The critical idea here is called a Protocol.A Protocol lets us specify the shape of objects that we expect to see.

    from typing import Protocol, TypeVar

	Self = TypeVar("Self, bound="Addable")

	class Addable(Protocol):
		def __add__(self: Self, other: Self) -> Self:
			...

	T = TypeVar("T", bound=Addable)

	def add(x: T, y: T) -> T:
		return x + y

	print(add("foo", "bar"))


This is a lot of machinery for such a simple example.
This allows us to refer to the type of objects that can be added to other objects of the same type to produce yet another object of that same type

We're going to take a look at a much more complex example than the add case that we explored above. 


    import asyncio
	inport functools
	import inspect
	inport time
	import typing import Final