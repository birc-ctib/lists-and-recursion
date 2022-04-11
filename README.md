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

and as you can see we use recursion here as part of defining the data structure. Such data structures are called *recursive*, when an object contains the same kind of objects, here a list containing another list in `tail`. If you have a list `x`, then you can get the head as `x.head` and the tail as `x.tail`.

To show you how we can write recursive functions on this kind of lists, here are two functions that compute the length of a list and the sum of its elements when they are integers:

```python
def length(x: List[T]) -> int:
    return 0 if x is None else 1 + length(x.tail)


def sum(x: List[int]) -> int:
    return 0 if x is None else x.head + sum(x.tail)
```


## List exercises

* Write a function, `contains`, that tells us whether an element is in a list. What is the runtime complexity?
* Write a function, `drop`, that removes the first `k` elements in a list. What is the runtime complexity?
* Write a function, `keep`, that returns a list of the first `k` elements in the input. What is the runtime complexity?
* Write a function, `append`, that appends an element to a list. Do not modify the original list but return a new list that consists of the original elements and then the new element. What is the runtime complexity?
* Write a function, `concat`, that concatenates two lists. Do not modify the original lists but return a new list that consists of the original elements from the two lists. What is the runtime complexity?
* Write a function, `rev`, that reverses a list. Do not modify the original list but return a new list that consists of the original elements in reverse order. What is the runtime complexity?

## Tail-recursion



[^1]: In the R programming language, that some of you might be familiar with, this kind of lists used to the main structure, way back in the elder days. The current lists are similar to Python's, but there are still some remnants of linked lists in R, used to handle function arguments. Languages that still use them are those where side-effects are not allowed, such as Haskell or SML, where linked lists give us an efficient way to still work with lists and to build persistent data structures. You will learn more about them later in the class.
