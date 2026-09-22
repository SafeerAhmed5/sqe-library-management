import pytest
from gradebook.gradebook import Roster, Student


@pytest.fixture
def empty_roster():
    # Function scope: a fresh roster is created for every test,
    # preventing tests from sharing or changing each other's data.
    return Roster()


@pytest.fixture
def student_with_scores():
    # Function scope: a fresh student is created for every test,
    # preventing tests from sharing or changing each other's data.
    student = Student("Ali", 101)
    student.add_score(80)
    student.add_score(90)
    return student


@pytest.fixture(scope="module")
def sample_students():
    # Module scope: useful for setup that can safely be shared
    # by all tests in one test module.
    student1 = Student("Ali", 101)
    student1.add_score(80)
    student1.add_score(90)

    student2 = Student("Sara", 102)
    student2.add_score(70)

    return [student1, student2]