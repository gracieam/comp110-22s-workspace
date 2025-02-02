"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730402215"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """When given a linked list and an index, return the data at that index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """When given a linked list, return the maximum data value."""
    if head is None:
        raise ValueError("Cannot call max with None.")
    else:
        if head.next is None:
            return head.data
        next_link = max(head.next)
        if head.data > next_link:
            return head.data
        else:
            return next_link


def linkify(items: list[int]) -> Optional[Node]:
    """Given a list of integers, return a linked list with the same values in the same order."""
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))
            

def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Returns a new linked list where each value from the input list is multiplied by the factor."""
    if head is None:
        return None
    else:
        if head.next is None:
            scaled: Node = Node(0, None)
            scaled.data = head.data * factor
            return scaled
        else:
            return Node(head.data * factor, scale(head.next, factor))