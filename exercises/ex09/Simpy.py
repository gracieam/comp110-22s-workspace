"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730402215"


class Simpy:
    """A class that has a single attribute of a list of floats along with many methods."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Intializes the values attribute of a newly constructed object to the argument passed in."""
        self.values = values

    def __str__(self) -> str:
        """Automagically called to convert an object to a str representation."""
        return f"Simpy({self.values})"

    def fill(self, value: float, N: int) -> None:
        """Fills in the values of an object with a specific number of repeating values, as indicated by the second parameter."""
        i: int = 0
        self.values = []
        while i < N:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in the values of an object with a range of values between the start and the stop parameter."""
        assert step != 0.0
        self.values = []
        while start < stop or stop < start:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        """Adds together all values in an object and returns the sum of those values."""
        result: float = 0.0
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """When given an expression with the add symbol, will return an evaulated object with values that are the result of self being added to the rhs."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs)
        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """When given an expression with the exponential symbol, will return an evaulated object with values that are the result of self being raised to the rhs."""
        result: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])   
        elif isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs)
        return Simpy(result)

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """When given an expression with an equals symbol, will return a list of bool that expresses whether a value is equal to the right hand side."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] == rhs)
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """When given an expression with greater than symbol, will return a list of bool that expresses whether a value is greater than the right hand side."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        elif isinstance(rhs, float):
            for i in range(0, len(self.values)):
                result.append(self.values[i] > rhs)
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Will allow a Simpy object to use subscription notation."""
        if isinstance(rhs, int):
            result: float = 0
            result = self.values[rhs]
            return result
        else:
            result_2 = Simpy([])
            assert len(self.values) == len(rhs)
            for i in range(0, len(self.values)):
                if rhs[i]:
                    result_2.values.append(self.values[i])
                
            return result_2