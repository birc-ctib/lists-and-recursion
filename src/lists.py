"""Linked lists."""

from __future__ import annotations
from typing import TypeVar, Generic, Optional
from dataclasses import dataclass

T = TypeVar('T')


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


List = Optional[L[T]]  # A list is an L() constructor or None


def length(x: List[T]) -> int:
    """
    Compute the length of x.

    >>> length(None)
    0
    >>> length(L(1, None))
    1
    >>> length(L(1, L(2, L(3, None))))
    3
    """
    return 0 if x is None else 1 + length(x.tail)


def sum(x: List[int]) -> int:
    """
    Compute the length of x.

    >>> sum(None)
    0
    >>> sum(L(1, None))
    1
    >>> sum(L(1, L(2, L(3, None))))
    6
    """
    return 0 if x is None else x.head + sum(x.tail)


def contains(x: List[T], e: T) -> bool:
    """
    Tell us if e is in x.

    >>> contains(L(1, L(2, L(3, None))), 4)
    False
    >>> contains(L(1, L(2, L(3, None))), 2)
    True
    """
    return False if x is None \
        else True if x.head == e \
        else contains(x.tail, e)


def drop(x: List[T], k: int) -> List[T]:
    """
    Remove the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 0)
    L(1, L(2, L(3, L(4, None))))
    >>> drop(x, 1)
    L(2, L(3, L(4, None)))
    >>> drop(x, 3)
    L(4, None)
    """
    if k == 0:
        return x
    assert x is not None, "We can't recurse on an empty list"
    return drop(x.tail, k - 1)


def keep(x: List[T], k: int) -> List[T]:
    """
    Keep only the first k elements.

    >>> x = L(1, L(2, L(3, L(4, None))))
    >>> keep(x, 0) # returns None but doesn't print
    >>> keep(x, 1)
    L(1, None)
    >>> keep(x, 3)
    L(1, L(2, L(3, None)))
    """
    if k == 0:
        return None
    assert x is not None, "Can't recurse on an empty list"
    return L(x.head, keep(x.tail, k - 1))


def concat(x: List[T], y: List[T]) -> List[T]:
    """
    Concatenate x and y.

    >>> concat(L(1, L(2, None)), L(3, L(4, None)))
    L(1, L(2, L(3, L(4, None))))
    """
    return y if x is None else L(x.head, concat(x.tail, y))


def append(x: List[T], e: T) -> List[T]:
    """
    Append e to x.

    >>> append(L(1, L(2, None)), 3)
    L(1, L(2, L(3, None)))
    """
    return concat(x, L(e, None))


def rev(x: List[T]) -> List[T]:
    """
    Reverse a list.

    >>> rev(L(1, L(2, L(3, None))))
    L(3, L(2, L(1, None)))
    """
    return None if x is None else append(rev(x.tail), x.head)
