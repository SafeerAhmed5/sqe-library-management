# Requirements Traceability Matrix (RTM)

| Requirement ID | Requirement | Test Case ID | Coverage |
|---|---|---|---|
| R1 | System shall accept valid scores | TC-01 | Covered |
| R2 | System shall reject negative scores | TC-02 | Covered |
| R3 | System shall reject non-numeric score input | TC-03 | Covered |
| R4 | System shall calculate correct average | TC-04, TC-06 | Covered |
| R5 | System shall safely handle an empty score list | TC-05 | Covered |
| R6 | System shall prevent duplicate roll numbers | TC-07 | Covered |
| R7 | System shall support case-insensitive name search | TC-08 | Covered |
| R8 | System shall accept boundary scores from 0 to 100 | TC-09, TC-10 | Covered |
| R9 | System shall assign correct grade letters | TC-11, TC-12 | Covered |

## Coverage Summary

All 9 identified requirements have at least one linked test case.

No requirement currently has zero test coverage.

## Gap Analysis

Some requirements are not implemented in the current GradeBook source code, including:

- Non-numeric score input handling
- Case-insensitive name search
- Grade-letter calculation

These requirements are still included in the RTM because they are part of the planned test scope. During test execution, their test cases will be marked **Blocked** if the required functionality is unavailable.

## Conclusion

The RTM provides traceability between requirements and test cases. Each requirement has at least one corresponding test case, allowing test coverage to be tracked during execution.