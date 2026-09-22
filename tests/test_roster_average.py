import pytest
from gradebook.gradebook import Roster


def test_class_average_empty():
    roster = Roster()

    # Act
    result = roster.class_average()

    # Assert
    assert result == 0.0


def test_class_average_single_student(student_with_scores):
    roster = Roster()
    roster.add_student(student_with_scores)

    # Act
    result = roster.class_average()

    # Assert
    assert result == pytest.approx(85.0)


def test_class_average_multiple_students(sample_students):
    roster = Roster()

    for student in sample_students:
        roster.add_student(student)

    # Act
    result = roster.class_average()

    # Assert
    assert result == pytest.approx(77.5)
