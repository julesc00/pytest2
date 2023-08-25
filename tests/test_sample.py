
import pytest
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Arrange phase, nothing to prepare here.

        # Act phase, call or do_something()

        # Assert phase, verify do_something() did what we expect.
        pass

    def test_one(self):
        pass

    def test_two(self):
        pass

    def test_two_part2(self):
        pass


class MySecondTestCase(unittest.TestCase):
    def test_two(self):
        pass


class ArimeticTests(unittest.TestCase):
    @staticmethod
    def test_sum_two_numbers():
        result = sum_two_numbers(3, 3)
        assert result == 6

    @staticmethod
    def test_3_values():
        result = sum_3_values(3, 3, 3)
        assert result == 9

    @staticmethod
    def test_3_values_wrong():
        result = sum_3_values(3, 1, 3)
        assert result != 9

    @staticmethod
    def test_3_values_zeroes():
        result = sum_3_values()
        assert result == 0


def sum_3_values(*args):
    total = 0
    for val in args:
        total += val
    return total


def sum_two_numbers(val1: int, val2: int) -> int:
    return val1 + val2


if __name__ == "__main__":
    pytest.main()
