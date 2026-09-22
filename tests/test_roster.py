import pytest
from gradebook.gradebook import Roster


class Student:
    def __init__(self, scores):
        self.scores = scores


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (3, False),
    (8, True),
])
def test_score_count_classes(score_count, expected_error):
    roster = Roster()
    student = Student([80] * score_count)

    if expected_error:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (1, False),
    (2, False),
    (5, False),
    (6, False),
    (7, True),
])
def test_score_count_boundaries(score_count, expected_error):
    roster = Roster()
    student = Student([80] * score_count)

    if expected_error:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)