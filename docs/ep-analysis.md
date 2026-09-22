# Equivalence Partitioning Analysis — GradeBook

## 1. Introduction

Equivalence Partitioning (EP) is a black-box testing technique that divides an input domain into classes where the system is expected to behave similarly. Instead of testing every possible value, one representative value is selected from each class. This reduces redundant test cases while maintaining useful test coverage.

## 2. Score Input — letter_grade(score)

The `letter_grade()` function converts a numeric score from 0 to 100 into a letter grade.

| Class | Input Range | Valid/Invalid | Representative Value | Expected Result |
|---|---|---|---:|---|
| Invalid-low | score < 0 | Invalid | -10 | ValueError |
| F | 0–59 | Valid | 45 | F |
| D | 60–69 | Valid | 65 | D |
| C | 70–79 | Valid | 75 | C |
| B | 80–89 | Valid | 85 | B |
| A | 90–100 | Valid | 95 | A |
| Invalid-high | score > 100 | Invalid | 150 | ValueError |

## 3. Number of Scores per Student

Business rule: A student must have between 1 and 6 scores.

| Class | Number of Scores | Valid/Invalid | Representative Value | Expected Result |
|---|---|---|---:|---|
| Invalid-low | 0 | Invalid | 0 | ValueError |
| Valid | 1–6 | Valid | 3 | Accepted |
| Invalid-high | 7+ | Invalid | 8 | ValueError |

## 4. Student Name

Business rule: A student name must be a non-empty string, maximum 50 characters, containing only letters, spaces, and hyphens.

| Class | Input | Valid/Invalid | Representative Value | Expected Result |
|---|---|---|---|---|
| Valid typical name | Normal name | Valid | Ali Khan | Accepted |
| Empty name | Empty string | Invalid | "" | ValueError |
| Over-length name | More than 50 characters | Invalid | 51-character name | ValueError |
| Digits/symbols | Contains numbers or symbols | Invalid | Ali123 | ValueError |

## 5. Equivalence Partitioning Limitation

Equivalence Partitioning selects representative values from each class, but it may miss defects located exactly at class boundaries. For example, an incorrect implementation might handle scores 59 and 60 incorrectly even though the representative value for the F class is 45. Therefore, Boundary Value Analysis will be needed to specifically test values at and around class boundaries.