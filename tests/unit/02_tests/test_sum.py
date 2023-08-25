
import pytest

from functs_02.sum_sample import sum_two_numbers


class ArimeticTests:
    @staticmethod
    def test_sum_two_numbers():
        result = sum_two_numbers(3, 3)
        assert result == 6


if __name__ == "__main__":
    pytest.main()
