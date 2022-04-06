"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730402215"


class Simpy:
    values: list[float]

    def __init__(self, values):
        self.values = values

    def __str__(self) -> str:
        return f"Simpy{self.values}"

    def fill(self, value: float, N: int) -> None:
        i: int = 0
        self.values = []
        while i < N:
            self.values.append(value)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        assert step != 0.0
        self.values = []
        while start < stop or stop < start:
            self.values.append(start)
            start += step

    def sum(self) -> float:
        result: float = 0.0
        result = sum(self.values)
        return result

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
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
    

