"""Unit Tests for Dictionary Module."""

__author__ = "730402215"

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
import pytest

def test_invert_same_length_word() -> None:
    """When given keys and values of the same length, the function should invert the keys and values."""
    my_dictionary: dict[str, str] = {"ate": "eat", "sat": "sit"}
    assert invert(my_dictionary) == {"eat": "ate", "sit": "sat"}


def test_invert_different_length_words() -> None:
    """When given keys and values of different lengths, the function should invert the keys and values."""
    my_dictionary: dict[str, str] = {"Gracie": "apple", "Logan": "orange"}
    assert invert(my_dictionary) == {"apple": "Gracie", "orange": "Logan"}


with pytest.raises(KeyError):
    """If values are the same in the given dictionary, then the function should return a KeyError when inverted."""
    my_dictionary: dict[str, str] = {"honeycrisp": "apple", "gala": "apple"}
    invert(my_dictionary)


def test_favorite_color_most_frequent() -> None:
    """When given colors in a dictionary, the function should return the name of the color seen most frequently."""
    my_dictionary: dict[str, str] = {"Gracie": "orange", "Clio": "orange", "Logan": "blue"}
    assert favorite_color(my_dictionary) == "orange"


def test_favorite_color_tied() -> None:
    """When two colors are seen the same number of times, the first one that appeared in the dictionary should be returned."""
    my_dictionary: dict[str, str] = {"Gracie": "green", "Clio": "blue", "Logan": "blue", "Lauren": "green"}
    assert favorite_color(my_dictionary) == "green"


def test_favorite_color_one_of_each() -> None:
    """When given three different colors, the one that appears first in the dictionary dhould be returned."""
    my_dictionary: dict[str, str] = {"Gracie": "orange", "Logan": "red", "Lauren": "blue"}
    assert favorite_color(my_dictionary) == "orange"


def test_count_right_number() -> None:
    """When given a list, a dictionary should be returned with the keys as the items in the list and values as the number of time the item appears."""
    my_list: list[str] = ["a", "a", "b", "c", "c", "c"]
    assert count(my_list) == {"a": 2, "b": 1, "c": 3}


def test_count_different_word_nonconsecutive() -> None:
    """When given a list with mutiple of the same items nonconsecutively, the correct value should be returned."""
    my_list: list[str] = ["dog", "cat", "parrot", "dog"]
    assert count(my_list) == {"dog": 2, "cat": 1, "parrot": 1}


def test_count_empty_list() -> None:
    """When given no list items, an empty dictionary should be returned."""
    my_list: list[str] = []
    assert count(my_list) == {}

