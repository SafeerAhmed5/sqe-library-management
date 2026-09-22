import pytest


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (3, False),
    (8, True),
])
def test_score_count_classes(score_count, expected_error, empty_roster):
    student = type("Student", (), {"scores": [80] * score_count})()

    if expected_error:
        with pytest.raises(ValueError):
            empty_roster.add_student(student)
    else:
        empty_roster.add_student(student)


@pytest.mark.parametrize('score_count,expected_error', [
    (0, True),
    (1, False),
    (2, False),
    (5, False),
    (6, False),
    (7, True),
])
def test_score_count_boundaries(score_count, expected_error, empty_roster):
    student = type("Student", (), {"scores": [80] * score_count})()

    if expected_error:
        with pytest.raises(ValueError):
            empty_roster.add_student(student)
    else:
        empty_roster.add_student(student)