def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score <= 59:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"


class GradeBookIOError(Exception):
    pass


class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.scores = []

    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")

        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0.0

        return sum(self.scores) / len(self.scores)


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        score_count = len(student.scores)

        if score_count < 1 or score_count > 6:
            raise ValueError("Student must have between 1 and 6 scores")

        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0

        return sum(student.average() for student in self.students) / len(self.students)

    def save_to_file(self, path):
        try:
            with open(path, "w") as file:
                for student in self.students:
                    scores = ", ".join(str(score) for score in student.scores)
                    file.write(
                        f"{student.name},{student.roll_number},{scores}\n"
                    )
        except OSError as error:
            raise GradeBookIOError(
                f"Unable to save roster to file: {path}"
            ) from error


def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")

    if len(name) == 0:
        raise ValueError("Name cannot be empty")

    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters")

    for char in name:
        if not (char.isalpha() or char in " -"):
            raise ValueError("Name can contain only letters, spaces, and hyphens")

    return True