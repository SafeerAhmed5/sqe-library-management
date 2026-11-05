# GradeBook Code Review Checklist

This checklist is used to review code quality before merging a Pull Request.

## 1. Correctness

- [ ] Does the function produce the expected output?
- [ ] Does it handle edge cases such as empty input and a single student?

## 2. Tests

- [ ] Are there tests for normal inputs and boundary conditions?
- [ ] Do the tests verify actual behavior rather than simply copying the implementation?

## 3. Readability

- [ ] Are variable and function names meaningful?
- [ ] Is the code properly formatted and documented with useful docstrings?

## 4. Design

- [ ] Does the new function follow the existing GradeBook architecture?
- [ ] Is unnecessary code duplication avoided?

## 5. Risk

- [ ] Could the changes break existing GradeBook functionality?
- [ ] Have invalid inputs and possible performance problems been considered?

## Lessons Learned

**Most valuable checklist item:**

Checking boundary conditions was especially valuable because it helped identify logic errors that ordinary test cases might miss.

**One item to add next time:**

Check whether error messages are clear and helpful when invalid input is provided.