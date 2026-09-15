# Software Test Plan — GradeBook

## 1. Test Plan Identifier

TP-GB-001

## 2. Introduction

This test plan defines the testing approach for the GradeBook system. The purpose is to verify that GradeBook correctly handles student scores, calculates averages, validates input, and prevents duplicate roll numbers.

## 3. Test Items

The following GradeBook functions will be tested:

- `addScore()`
- `addStudent()`
- `calculateAverage()`

## 4. Features to Be Tested

The following features are included in testing:

1. Adding valid scores
2. Rejecting negative scores
3. Handling empty score lists
4. Calculating average scores
5. Adding students with roll numbers
6. Rejecting duplicate roll numbers
7. Handling boundary scores such as 0 and 100
8. Handling invalid input

## 5. Features Not to Be Tested

Student name search and grade-letter calculation are not tested because the current GradeBook implementation does not provide these features. Testing will focus only on functionality currently implemented in the code.

## 6. Test Approach

Testing will mainly use functional and black-box testing techniques.

The tests will include:

- Positive test cases
- Negative/error test cases
- Boundary value tests
- Input validation tests
- Regression tests for previously fixed defects

## 7. Test Environment

- Programming Language: Java
- IDE/Editor: Visual Studio Code
- Operating System: Windows
- Version Control: Git and GitHub
- Application Under Test: GradeBook

## 8. Entry Criteria

Testing can begin when:

- GradeBook source code is available.
- Required Java files compile successfully.
- Test cases have been prepared.

## 9. Exit Criteria

Testing will be considered complete when:

- All 12 planned test cases have been executed.
- At least 90% of test cases pass.
- All critical defects are fixed or documented.
- Test execution results are recorded.

## 10. Pass/Fail Criteria

A test case is **PASS** when the actual result matches the expected result.

A test case is **FAIL** when the actual result differs from the expected result.

Overall testing passes when at least **90% of the 12 test cases pass** and no critical defect remains unresolved.

## 11. Test Deliverables

The following documents will be produced:

- Test Plan
- Test Cases
- Requirements Traceability Matrix (RTM)
- Test Execution Results
- GitHub Issues for failed test cases

## 12. Risks and Assumptions

### Risks

- Some required features may not exist in the current implementation.
- Invalid inputs may cause unexpected behavior.
- Previously fixed defects may reappear.

### Assumptions

- The Java environment is correctly configured.
- The current GradeBook source code represents the version being tested.
- Test results will be recorded accurately.

## 13. Approval

This test plan is prepared for the Software Quality Engineering Lab 4 testing activities.