import pytest


def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()

    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)

    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()

    assert accum.count == 2


def test_accumulator_cannot_set_count_directly(accum):
    """Arrange-act-assert"""
    with pytest.raises(
        AttributeError,
        match=r"can't set attribute 'count'"
    ) as error:
        accum.count = 10
