"""Tests for linked list utils."""

from exercises.ex10.linked_list import Node, is_equal, last, value_at, max, linkify, scale
import pytest

__author__ = "730402215"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a value error."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return a reference to its last Node."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_return_data() -> None:
    """Given a Node and an index, return the data at the given index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_index_error() -> None:
    """Index error should be raised if index does not exist when given an index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    with pytest.raises(IndexError):
        value_at(linked_list, 4)


def test_max_return_max() -> None:
    """Given a Node, return the maximum data value in the linked list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max_empty() -> None:
    """If the given linked list is empty, raise a value error."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_items() -> None:
    """If given list has values, return a linked list of the given values in order."""
    items = [1, 2, 3]
    assert is_equal(linkify(items), Node(1, Node(2, Node(3, None))))


def test_linkify_empty() -> None:
    """If given an empty list, return None."""
    items: list = []
    assert linkify(items) is None


def test_scale_items() -> None:
    """If given a linked list with values, return a new list multiplied by the given factor."""
    linked_list = linkify([1, 2, 3])
    assert is_equal(scale(linked_list, 2), Node(2, Node(4, Node(6, None))))


def test_scale_empty() -> None:
    """If given an empty linked list, return None."""
    linked_list = linkify([])
    assert scale(linked_list, 2) is None
