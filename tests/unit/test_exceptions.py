import pytest


def test_divide_by_zero():
    """
    Strategy:
        Here I can make the == assertion to view the exception raised and then copy the message
        at error.value and make a comparison within pytest.raises(): as in the example.

        This approach will help choose the proper raised exception by Python.
    """
    with pytest.raises(ZeroDivisionError) as error:
        num = 1 / 0

        assert "division by zero" in str(error.value)
