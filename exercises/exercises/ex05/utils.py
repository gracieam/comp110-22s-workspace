"""Using 'list' Utility Functions."""

__author__ = "730402215"

def only_evens(given_list: list[int]) -> list:
    """When given a list of even numbers, the even numbers are returned."""
    even_list: list[int] = list()
    i: int = 0
    while i < len(given_list):
        if given_list[i] % 2 == 0:
            even_list.append(given_list[i])
        i += 1
    return even_list

def sub(given_list: list[int], start: int, end: int) -> list:
    """When given a list and two indexes, a subset list should be returned with values between the start and end index (not inclusive)."""
    subset_list: list[int] = list()
    if start < 0:
        start = 0
    if end > len(given_list):
        end = (len(given_list) - 1)
    end -= 1
    if len(given_list) == 0 or start > len(given_list) or end <= 0:
        return subset_list
    i: int = start
    while i <= end:
       subset_list.append(given_list[i])
       i += 1
    return subset_list


def concat(list_one: list[int], list_two: list[int]) -> list:
    """When given two lists, a list should be returned containing all of the elements in the first list and the second list in order"""
    new_list = list_one + list_two
    return new_list
