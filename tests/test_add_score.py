import pytest
from gradebook.gradebook import Student


@pytest.mark.parametrize(
    "score, expected_error",
    [
        (0, False),
        (1, False),
        (50, False),
        (99, False),
        (100, False),
        (-1, True),
        (101, True),
    ],
    ids=[
        "minimum-valid",
        "low-valid",
        "middle-valid",
        "high-valid",
        "maximum-valid",
        "below-minimum",
        "above-maximum",
    ],
)
def test_add_score_cases(score, expected_error):
    student = Student("Ali", 101)

    if expected_error:
        with pytest.raises(ValueError):
            student.add_score(score)
    else:
        student.add_score(score)
        assert score in student.scores