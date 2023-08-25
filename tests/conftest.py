import pytest

from more_stuff.accum import Accumulator


@pytest.fixture
def accum():
    return Accumulator()
