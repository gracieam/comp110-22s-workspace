"""Testing 'list' Utility Functions."""

__author__ = "730402215"

from exercises.exercises.ex05.utils import only_evens

def test_only_evens_searching() -> None:
    """When given a list of even numbers, only the even numbers are returned."""
    given_list: list[int] = [1, 2, 3, 4,]
    assert only_evens(given_list) == [2, 4] 

def test_only_evens_no_odds() -> None:
    """When given a list of odd numbers, an empty list should be returned."""
    given_list: list[int] = [1, 3, 5]
    assert only_evens(given_list) == []

def test_only_evens_repeats() -> None:
    """When repeat numbers are in a list, the function returns each of the repeated number"""
    given_list: list[int] = [4, 4, 4]
    assert only_evens(given_list) == [4, 4, 4]

from exercises.exercises.ex05.utils import sub

def test_sub_index() -> None:
    """When given a list and two indexes, a sublist should be returned."""
    given_list: list[int] = [10, 20, 30, 40]
    assert sub(given_list, 1, 3) == [20, 30]

def test_sub_repeats() -> None:
    """When given a list that repeats within the start and end, the repeated value is returned."""
    given_list: list[int]  = [5, 10, 10, 15, 20]
    assert sub(given_list, 1, 4) == [10, 10, 15]

def test_sub_long_start() -> None:
    """When given a start that is greater than the length of the list, an empty list is returned."""
    given_list: list[int] = [10, 20 , 30]
    assert sub(given_list, 3, 4) == []

from exercises.exercises.ex05.utils import concat

def test_concat_in_order() -> None:
    """When given two lists, the second list is concatenated on the end of the first list."""
    list_one: list[int] = [1, 2, 3, 4, 5]
    list_two: list[int] = [6, 7, 8, 9, 10]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_concat_no_mutation() -> None:
    """When given two lists, the second list is concatenated on the end of the first list without mutating either list"""
    list_one: list[int] = [1, 3, 5]
    list_two: list[int] = [2, 4, 6]
    assert concat(list_one, list_two) == [1, 3, 5, 2, 4, 6]

def test_concat_empty_returns_empty() -> None:
    "When given two empty lists, an empty list is returned"
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []

