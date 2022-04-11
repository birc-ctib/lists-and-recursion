"""Linked lists."""

from __future__ import annotations
from typing import TypeVar, Generic
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


List = L[T] | None


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
    return L(x.head, keep(x.tail, k - 1))


def list_cases(x: List[T]) -> str:
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
