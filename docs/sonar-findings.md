
# Lab 10 – Static Code Analysis with SonarCloud

## 1. Objective
To perform static code analysis using SonarCloud and identify potential code-quality issues.

## 2. Analysis Configuration
- Tool: SonarCloud
- Project: sqe-library-management
- Configuration file: sonar-project.properties
- Python version: 3.14
- Source directories: gradebook, libraryhub
- Test directory: tests

## 3. SonarCloud Analysis Results

- Lines of Code: 311
- Reported Issues: 0
- Security Issues: 0
- Reliability Issues: 0
- Maintainability Issues: 0
- Duplications: 0.0%
- Quality Gate: Not computed

## 4. Analysis Warnings

SonarCloud reported two configuration warnings:

1. Python version should be explicitly configured using sonar.python.version.
2. Test files should be identified using sonar.tests.

Both settings have been added to sonar-project.properties. A new analysis is still required to verify that the warnings are resolved.

## 5. Test Verification

Command:
python -m pytest -q

Result:
60 tests passed.

## 6. Conclusion

The SonarCloud project configuration has been added and pushed to GitHub. The existing automated test suite passes successfully.

Further verification is required to confirm the latest branch analysis, resolve the analysis warnings, and obtain a computed Quality Gate status.
