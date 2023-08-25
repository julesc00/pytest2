import pytest

from book_python_testing.tasks import Task


"""
-m MARKEXPR

Markers are one of the best ways to mark a subset of your test functions so that they can be run
together. As an example, one way to run `test_replace()` and `test_member_access()`, even though
they are in separate files, is to mark them.
You can use any marker name. Let’s say you want to use run_these_please. You’d mark a test
using the decorator `@pytest.mark.run_these_please`, like so.

Then you’d do the same for test_replace(). You can then run all the tests with the same marker
with `pytest -m run_these_please`:
"""


def test_as_dict():
    """
    _asdict() should return a dictionary
    """
    t_task = Task("do something", "Julio", True, 21)
    t_dict = t_task._asdict()
    expected = {
        "summary": "do something",
        "owner": "Julio",
        "done": True,
        "id": 21
    }

    assert t_dict == expected


@pytest.mark.run_this_please
def test_replace():
    """replace() should change passed in fields."""
    task_before = Task("finish book", "Jemima", False)
    task_after = task_before._replace(id=10, done=True)
    task_expected = Task("finish book", "Jemima", True, 10)

    assert task_after == task_expected


def test_defaults():
    """Using no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2
