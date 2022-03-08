"""Dictionary related utility functions."""

__author__ = "730402215"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    result: list[dict[str,str]] = []
    for row in table:
        print("todo")
    return []