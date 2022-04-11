# Lists and recursion

Python's lists, that we can index into in constant time, but where it takes linear time to add or remove in the middle of a list, is a data structure known as a *dynamic array* or a *dynamic list*. There are other kinds of lists, and one of them, the *linked lists* is used in many other programming languages, especially functional languages.[^1]

With the kind of linked lists I have in mind you can do one of two things: you can get the value at the front of a list, or you can get a reference to the rest of the list.

I have defined such a list for you:

```python
@dataclass
class L(Generic[T]):
    """
    A single link in a linked list.

    The `head` attribute gives you the value at the head of
    this list while `tail` gives you the rest of the list,
    or None if the rest is the empty list.

    >>> L(1, L(2, L(3, None)))
    L(1, L(2, L(3, None)))
    """

    head: T
    tail: List[T]

    def __repr__(self) -> str:
        """Representation of this object."""
        return f"L({self.head}, {self.tail})"


# A list is either an L(head, tail) or None
List = L[T] | None
```

The details of this definition is not something you need to understand right now, but it defines a list over some generic type `T` (you can use any type you want, like `int`, of `str` or whatever). If you have a list `x`, then `x.head` gives you the value at the front of the list, similar to `x[0]` for a Python list, and `x.tail` gives you the rest of the list, like `x[1:]` except that `x.tail` takes constant time while `x[1:]` takes linear time.

You can create a list of the numbers 1, 2, and 3 with

```python
x = L(1, L(2, L(3, None)))
```

and as you can see we use recursion here as part of defining the data structure. Such data structures are called *recursive*, when an object contains the same kind of objects, here a list containing another list in `tail`.

If you want to write a recursive function on a list, a convinient way is to use patter matching. This isn't described in the book (because it wasn't part of Python when the book came out), but it looks like this:

```python
def list_cases(x: L[T]) -> str:
    """
    Output which of three cases we have.

    >>> list_cases(None)
    'x is empty'
    >>> list_cases(L(42, None))
    'x is one long and the value at the head is 42'
    >>> list_cases(L(13, L(42, None)))
    'x is more than one long and the value at the head is 13'
    """
    match x:
        case None:
            return "x is empty"
        case L(h, None):
            return f"x is one long and the value at the head is {h}"
        case L(h, _):
            return f"x is more than one long and the value at the head is {h}"
```

The `match x` means that we will have different cases that will look at the structure of `x`. The `case ...` then tries to matches against the different structures. With `case None` we will match `None`, so we enter that part with an empty list. With `case L(h, None)` we will match a list where `tail` is `None`, so a list with a single argument. the variable `h` will be bound to the head of the list, so we can see the value of `head` that way. The last case, `case L(h, _)` matches any `x` that is a `L`-object, but since `L(h, None)` is matched first, the cases where the list has length one will be caught there, which means that `L(h, _)` is only matched when we have a longer list.

I hope that makes sense; otherwise, study it a bit more. It is a very nice way of handing recursion in general and is widely used in many programming languages (and now also in Python).

To show you how we can write recursive functions on this kind of lists, here are two functions that compute the length of a list and the sum of its elements when they are integers:

```python
def length(x: L[T]) -> int:
    """
    Compute the length of x.

    >>> length(None)
    0
    >>> length(L(1, None))
    1
    >>> length(L(1, L(2, L(3, None))))
    3
    """
    match x:
        case None: return 0
        case L(_, t): return 1 + length(t)


def sum(x: L[int]) -> int:
    """
    Compute the length of x.

    >>> sum(None)
    0
    >>> sum(L(1, None))
    1
    >>> sum(L(1, L(2, L(3, None))))
    6
    """
    match x:
        case None: return 0
        case L(h, t): return h + sum(t)
```

If you don't want to pattern match, however, and you do not always want to do that, then `x.head` and `x.tail` gives you the two attributes.


## List exercises

* Write a function, `drop`, that removes the first `k` elements in a list. What is the runtime complexity?
* Write a function, `keep`, that returns a list of the first `k` elements in the input. What is the runtime complexity?


## Tail-recursion



[^1]: In the R programming language, that some of you might be familiar with, this kind of lists used to the main structure, way back in the elder days. The current lists are similar to Python's, but there are still some remnants of linked lists in R, used to handle function arguments. Languages that still use them are those where side-effects are not allowed, such as Haskell or SML, where linked lists give us an efficient way to still work with lists and to build persistent data structures. You will learn more about them later in the class.
