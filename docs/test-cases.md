# GradeBook Test Cases

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |
|---|---|---|---|---|---|---|---|
| TC-01 | Add valid score | R1: System shall accept valid scores | GradeBook object is available | 1. Create GradeBook<br>2. Add score 75 | Score is accepted without error | High | Functional |
| TC-02 | Reject negative score | R2: System shall reject negative scores | GradeBook object is available | 1. Create GradeBook<br>2. Add score -10 | `IllegalArgumentException` is thrown | High | Negative |
| TC-03 | Handle non-numeric score | R3: System shall reject non-numeric score input | User input is required | 1. Enter `abc` as score | Non-numeric input is rejected | Medium | Negative |
| TC-04 | Calculate average with multiple scores | R4: System shall calculate correct average | GradeBook object is available | 1. Add 60<br>2. Add 80<br>3. Calculate average | Average is 70.0 | High | Functional |
| TC-05 | Calculate average with empty list | R5: System shall safely handle empty score list | New GradeBook object | 1. Create GradeBook<br>2. Calculate average | Average returned is 0.0 and no crash occurs | High | Regression |
| TC-06 | Calculate average with single score | R4: System shall calculate correct average | GradeBook object is available | 1. Add score 85<br>2. Calculate average | Average is 85.0 | Medium | Boundary |
| TC-07 | Reject duplicate roll number | R6: System shall prevent duplicate roll numbers | GradeBook object is available | 1. Add student with roll number 101<br>2. Add another student with roll number 101 | `IllegalArgumentException` is thrown | High | Negative |
| TC-08 | Case-insensitive name search | R7: System shall support case-insensitive name search | Name search feature exists | 1. Search using different letter case | Matching student is found regardless of case | Medium | Functional |
| TC-09 | Accept maximum score | R8: System shall accept score 100 | GradeBook object is available | 1. Add score 100 | Score 100 is accepted | Medium | Boundary |
| TC-10 | Accept minimum score | R8: System shall accept score 0 | GradeBook object is available | 1. Add score 0 | Score 0 is accepted | Medium | Boundary |
| TC-11 | Grade-letter mid-range | R9: System shall assign correct grade letter | Grade calculation feature exists | 1. Provide a mid-range score<br>2. Calculate grade | Correct grade letter is returned | Medium | Functional |
| TC-12 | Grade-letter boundary | R9: System shall correctly handle grade boundaries | Grade calculation feature exists | 1. Provide a score at a grade boundary<br>2. Calculate grade | Correct grade letter for the boundary is returned | High | Boundary |
## Test Execution Results

| Test Case | Result | Execution Note |
|---|---|---|
| TC-01 | PASS | Valid score 75 was accepted successfully. |
| TC-02 | PASS | Negative score was correctly rejected. |
| TC-03 | BLOCKED | Non-numeric input handling is not implemented in the current GradeBook. |
| TC-04 | PASS | Average of 60 and 80 was correctly calculated as 70.0. |
| TC-05 | PASS | Empty score list correctly returned 0.0 without crashing. |
| TC-06 | PASS | Single score 85 correctly returned an average of 85.0. |
| TC-07 | PASS | Duplicate roll number was correctly rejected. |
| TC-08 | BLOCKED | Case-insensitive name search is not implemented. |
| TC-09 | PASS | Maximum score 100 was accepted successfully. |
| TC-10 | PASS | Minimum score 0 was accepted successfully. |
| TC-11 | BLOCKED | Grade-letter calculation is not implemented. |
| TC-12 | BLOCKED | Grade-letter boundary calculation is not implemented. |

## Execution Summary

- Total Test Cases: 12
- Passed: 8
- Failed: 0
- Blocked: 4
- Pass Rate of Executed Tests: 100%

The blocked test cases are related to functionality that is not currently implemented in the GradeBook source code.