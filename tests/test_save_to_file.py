import pytest
from gradebook.gradebook import Roster, Student, GradeBookIOError


def test_save_to_file_writes_content(mocker):
    roster = Roster()

    student = Student("Ali", 101)
    student.add_score(80)
    student.add_score(90)
    roster.add_student(student)

    mock_file = mocker.mock_open()
    mocker.patch("builtins.open", mock_file)

    roster.save_to_file("students.txt")

    mock_file.assert_called_once_with("students.txt", "w")
    mock_file().write.assert_called_once_with("Ali,101,80, 90\n")


def test_save_to_file_handles_os_error(mocker):
    roster = Roster()

    mocker.patch(
        "builtins.open",
        side_effect=OSError("Disk error")
    )

    with pytest.raises(GradeBookIOError):
        roster.save_to_file("students.txt")