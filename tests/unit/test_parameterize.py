import pytest

from functs_02.sum_sample import sum_two_numbers


"""
Parameterized test cases
"""

products = (
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
)


@pytest.mark.parametrize("a, b, product", products)
def test_multiplication(a, b, product):
    assert a * b == product


results = (
    (7, 3, 10),
    ("hello", " world", "hello world"),
    (10.5, 25.5, 36.0)
)


@pytest.mark.parametrize("val1, val2, result", results)
def test_sum_two_numbers(val1, val2, result):
    """
    From youtube video at: https://www.youtube.com/watch?v=7qMhuVGqGY4
    """
    assert sum_two_numbers(val1, val2) == result
