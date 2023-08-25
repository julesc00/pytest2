import pytest
import os

from functs_02.get_student_data import StudentDB


@pytest.fixture(scope="module")
def db():
    db = StudentDB()
    db.connect("students.json")
    yield db
    print("closing db")
    db.close()


def test_jemima_data(db):
    jemima_data = db.get_data("Jemima")

    assert jemima_data["id"] == 1


def test_charbel_data(db):
    charbel_data = db.get_data("Charbel")

    assert charbel_data["id"] == 2
