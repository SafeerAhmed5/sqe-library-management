# Unit Testing Notes - Lab 7

## 1. Unit Testing

Unit testing verifies small, testable parts of a program independently.

This lab uses pytest to test the GradeBook system. The tests follow the Arrange-Act-Assert (AAA) pattern:

- Arrange: prepare the required data and objects.
- Act: call the function or method being tested.
- Assert: verify the expected result.

---

## 2. Pytest Fixtures

Fixtures provide reusable test setup and reduce duplication.

### Function Scope

The default fixture scope is `function`.

A function-scoped fixture creates fresh test data for every test. This is useful when tests should remain independent and should not share changes to the same object.

Example:

`student_with_scores` creates a new Student for each test.

### Module Scope

A module-scoped fixture is created once for the test module.

This is useful for expensive setup that can safely be shared by multiple tests when the data does not need to be recreated for every test.

Example:

`sample_students` is shared by tests in the module.

---

## 3. Verbose Pytest Output

Command:

`pytest -v tests/`

Verbose mode displays each individual test and its result.

It is useful when:

- checking exactly which tests ran
- identifying the specific test that failed
- reviewing parametrized test cases
- demonstrating test execution during development or grading

Final result:

55 passed

---

## 4. Short Traceback Output

Command:

`pytest --tb=short`

The `--tb=short` option displays a shorter traceback when a test fails.

It is useful when:

- quickly locating the source of a failure
- reducing unnecessary traceback details
- reviewing test failures in a compact format

Verbose output is better for detailed test execution, while short traceback output is useful for quickly understanding failures.

---

## 5. Mocking

The `pytest-mock` plugin provides the `mocker` fixture.

In this lab, `open()` is mocked so that `save_to_file()` can be tested without creating a real file.

Mocking is useful for isolating a unit from external dependencies such as files, databases, or network services.

The tests also verify that an `OSError` is converted into the custom `GradeBookIOError`.

---

## 6. Parametrized Testing

`@pytest.mark.parametrize` allows multiple input cases to be tested using one test function.

The `add_score()` boundary and validation tests use seven documented cases:

- minimum valid score
- low valid score
- middle valid score
- high valid score
- maximum valid score
- below minimum
- above maximum

Using `ids=` makes each case clearly identifiable in pytest output.

---

## 7. Final Test Result

The complete test suite was executed successfully.

Result:

55 tests passed.

The suite includes tests from Labs 5-6 as well as the new Lab 7 unit tests.