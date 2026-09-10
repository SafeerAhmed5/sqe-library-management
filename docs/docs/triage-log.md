# Triage Meeting Log

## Sprint Defect Prioritization

| Rank | Issue | Defect | Severity | Priority | Decision |
|---|---|---|---|---|---|
| 1 | Issue #1 | GradeBook crashes with empty score list | High | High | Fix this sprint |
| 2 | Issue #2 | GradeBook accepts negative scores | High | High | Fix this sprint |
| 3 | Issue #3 | GradeBook allows duplicate roll numbers | High | High | Fix this sprint |
| 4 | Issue #4 | GradeBook calculates averages with incorrect rounding | Medium | Medium | Won't fix this sprint |
| 5 | Issue #5 | GradeBook name search is case-sensitive | Low | Medium | Won't fix this sprint |

## Triage Decisions

### 1. Empty Score List Crash
This is ranked first because it can cause the application to fail during a core operation. It has both high severity and high priority, so it should be fixed immediately.

### 2. Negative Scores Accepted
This is ranked second because it allows invalid data to enter the GradeBook and can affect student grades. It has high severity and high priority.

### 3. Duplicate Roll Numbers
This is ranked third because duplicate roll numbers can create conflicting student records. Although it is high severity and high priority, the empty-score crash and invalid-score problem are considered more urgent for this sprint.

### 4. Incorrect Average Rounding
This issue has medium severity and medium priority. It causes inaccurate displayed averages, but the application remains usable, so it is deferred to a future sprint.

### 5. Case-Sensitive Name Search
This issue has low severity but medium priority because it mainly affects usability. It does not corrupt data or crash the application, so it is deferred to a future sprint.

## Severity vs Priority Trade-offs

### Trade-off 1 — Duplicate Roll Numbers vs Empty Score List Crash
Both issues have high severity and high priority. The empty-score crash is ranked higher because it can directly stop a core GradeBook operation, while duplicate roll numbers mainly create data-quality problems.

### Trade-off 2 — Case-Sensitive Search vs Average Rounding
The name-search defect has low severity but medium priority because it affects usability. The rounding defect has medium severity and medium priority because it produces inaccurate academic results. Therefore, the rounding issue is ranked higher even though both are deferred.

## Sprint Decision

Issues #1, #2, and #3 will be fixed during this sprint.

Issues #4 and #5 will not be fixed this sprint because they have lower immediate impact and can be addressed in a future sprint.
