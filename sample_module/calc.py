from statistics import mean
from functools import cached_property


"""
We use `cached_property` whenever we use an expensive function and the result is always the same and use it
in several places.
"""


class Calculator:
    def __init__(self, values: list[float]):
        self.values = values

    @cached_property
    def sum(self) -> float:
        print(f"Getting the sum of: {self.values}")
        return sum(self.values)

    @cached_property
    def mean(self) -> float:
        print(f"Getting the mean of: {self.values}")
        return mean(self.values)


if __name__ == "__main__":
    calc = Calculator([1.2, 2.5, 3.3, 4.9, 5.5])
    print(calc.sum)
    print(calc.sum)
    print(calc.mean)
    print(calc.mean)


