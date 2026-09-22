# Boundary Value Analysis - Lab 6

## 1. Introduction

Boundary Value Analysis (BVA) is a black-box testing technique that focuses on values at and around the boundaries of input ranges. It complements Equivalence Partitioning by testing values immediately below, at, and immediately above important boundaries.

---

## 2. letter_grade(score)

From Lab 5, the valid score domain is 0-100.

| Boundary | Value - 1 | Value | Value + 1 | Expected Results |
|---|---:|---:|---:|---|
| Minimum score 0 | -1 -> ValueError | 0 -> F | 1 -> F | ValueError, F, F |
| F/D boundary 60 | 59 -> F | 60 -> D | 61 -> D | F, D, D |
| D/C boundary 70 | 69 -> D | 70 -> C | 71 -> C | D, C, C |
| C/B boundary 80 | 79 -> C | 80 -> B | 81 -> B | C, B, B |
| B/A boundary 90 | 89 -> B | 90 -> A | 91 -> A | B, A, A |
| Maximum score 100 | 99 -> A | 100 -> A | 101 -> ValueError | A, A, ValueError |

---

## 3. Roster Score-Count Rule

From Lab 5, a student must have between 1 and 6 scores.

| Boundary | Value - 1 | Value | Value + 1 | Expected Results |
|---|---:|---:|---:|---|
| Minimum score count 1 | 0 -> ValueError | 1 -> Accepted | 2 -> Accepted | ValueError, Accepted, Accepted |
| Maximum score count 6 | 5 -> Accepted | 6 -> Accepted | 7 -> ValueError | Accepted, Accepted, ValueError |

---

## 4. validate_name(name)

From Lab 5, the name must not be empty and must have a maximum length of 50 characters.

| Boundary | Value - 1 | Value | Value + 1 | Expected Results |
|---|---:|---:|---:|---|
| Minimum length 0 | N/A | 0 -> ValueError | 1 -> Accepted | ValueError, Accepted |
| Maximum length 50 | 49 -> Accepted | 50 -> Accepted | 51 -> ValueError | Accepted, Accepted, ValueError |

Additional required boundary lengths:

| Name Length | Expected Result |
|---:|---|
| 0 | ValueError |
| 1 | Accepted |
| 49 | Accepted |
| 50 | Accepted |
| 51 | ValueError |

---

## 5. BVA and Equivalence Partitioning

Equivalence Partitioning selects representative values from valid and invalid classes. Boundary Value Analysis focuses specifically on the edges of those classes.

For example, EP used 45 as a representative value for the F grade. BVA additionally tests 59, 60, and 61 to verify the exact F/D boundary.

Therefore, combining EP and BVA provides better coverage of both general input classes and boundary conditions.

---

## 6. Testing Results

All boundary-focused tests were executed using pytest.

Final complete test suite result: 43 passed in 0.46s.

The tested boundaries for letter_grade(), Roster, and validate_name() all behaved according to their expected results.

No genuine off-by-one or other boundary defect was discovered during the BVA testing.

Because no genuine defect was found, no defect was artificially introduced or fabricated for the purpose of satisfying the lab requirement.

---

## 7. Testing Objective

The purpose of the Lab 6 tests is to verify that:

- score boundaries are handled correctly by letter_grade()
- the 1-6 score-count rule is handled correctly by Roster
- the 0 and 50 character name-length boundaries are handled correctly by validate_name()
- no off-by-one errors exist at the tested boundaries