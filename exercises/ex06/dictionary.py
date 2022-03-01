"""Dictionary Functions"""

__author__ = "730402215"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values when given a dictionary."""
    inverted_dictionary: dict[str, str] = dict()
    for key in my_dictionary:
        value: str = my_dictionary[key]
        if value in inverted_dictionary:
            raise KeyError("Key is repeated!")
        else:
            inverted_dictionary[value] = key
    return inverted_dictionary
    

def favorite_color(my_dictionary: dict[str, str]) -> str:
    """When given a dictionary containing names of colors, the name of the most frequent color is returned."""
    i: int = 0
    empty_dictionary: dict[str, int] = dict()
    max: int = 0
    result: str = ""
    for key in my_dictionary:
        empty_dictionary[my_dictionary[key]] = 0
    for key in my_dictionary:
        empty_dictionary[my_dictionary[key]] += 1
    for key in empty_dictionary:
        if empty_dictionary[key] > max:
            max = empty_dictionary[key]
            result = key
    return result
        

def count(my_list: list[str]) -> dict[str, int]: 
    """When given a list, a dictionary should be returned that comtains the list value as key and the instances of that list value as a value."""
    dictionary: dict[str, int] = dict()
    i: int = 0
    for item in my_list:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary