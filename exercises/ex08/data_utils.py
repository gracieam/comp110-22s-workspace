"""Utility functions to organize data."""

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
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column_name]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table reprsented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column_name in first_row:
        result[column_name] = column_values(row_table, column_name)
    return result


def head(col_table: dict[str, list[str]], row_N: int) -> dict[str, list[str]]:
    """Produced a new column table with N rows of data per column."""
    result: dict[str, list[str]] = {}
    for column_name in col_table:
        N_value: list[str] = []
        i: int = 0
        if row_N >= len(col_table):
            return col_table
        while i < row_N:
            N_value.append(col_table[column_name][i])
            i += 1
        result[column_name] = N_value
    return result


def select(col_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Return a new column table with only a specific subset of columns on the orginal given table."""
    new_col_table: dict[str, list[str]] = {}
    for column_name in columns:
        column_value: list[str] = col_table[column_name]
        new_col_table[column_name] = column_value
    return new_col_table


def concat(col_t1: dict[str, list[str]], col_t2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines two column-based tables and returns the combined result."""
    combined: dict[str, list[str]] = {}
    for column in col_t1:
        combined[column] = col_t1[column]
    for column in col_t2:
        if column in combined and col_t2[column] != col_t1[column]:
            combined[column] += col_t2[column]
        else:
            combined[column] = col_t2[column]
    return combined


def count(input_list: list[str]) -> dict[str, int]:
    """Returns a value where keys are the items in a list and values are the frequency of those items."""
    result: dict[str, int] = {}
    for item in input_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def filter(col_table: dict[str, list[str]], column_n1: str, column_n2: str) -> dict[str, list[str]]:
    filtered: dict[str, list[str]] = {}
    response_list: list[str] = []
    difficulty_list: list[str] =[]
    column_value: list[str] = col_table[column_n1]
    i: int = 0
    while i < len(column_value):
        if column_value[i] == "None to less than one month!" or column_value[i] == "Over 2 years":
            response_list.append(column_value[i])
            difficulty_list.append(col_table[column_n2][i])
        i += 1
    filtered[column_n1] = response_list
    filtered[column_n2] = difficulty_list     
    return filtered

# def combined(col_table: dict[str, list[str]], col_1: str, col_2: str) -> dict[str, str]:
#     combined: dict[str, str] = {}
    
    
#     return combined

# def separate(col_table: dict[str, list[str]], col_n: str) -> list[str]:
#     separated: list[str] = []
#     for col_n in col_table:
#         for value in col_n:
#             separated.append(value)
#     # i: int = 0
#     # column_value: list[str] = col_table[col_n]
#     # while i < len(column_value):
#     #     separated.append(column_value[i])
#     #     i += 1         
#     return separated
    
    

