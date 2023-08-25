import pytest

import book_python_testing.tasks


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnect after."""
    # Setup: start db
    tasks
