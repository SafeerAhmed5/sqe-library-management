# TDD Log — Rank Books by Popularity

## Feature
Implement `rank_books_by_popularity(library)` to return books in descending order of borrowing count. When borrowing counts are equal, books are sorted alphabetically by title.

## Cycle 1 — Empty Catalog

- **RED:** Added a test to verify that an empty catalog returns an empty list.
- **RED commit:** `019a40d`
- **GREEN:** Implemented the initial function returning an empty list.
- **GREEN commit:** `829cafa`
- **Result:** The empty catalog test passed.

## Cycle 2 — Single Book

- **RED:** Added a test to verify that a library containing one book returns that book.
- **RED commit:** `8a1dce0`
- **GREEN:** Updated the function to return the library's books.
- **GREEN commit:** `a5083e0`
- **Result:** The single-book test passed.

## Cycle 3 — Multiple Books

- **Test:** Added a test to verify that books are sorted by borrowing count in descending order.
- **Commit:** `5a28557`
- **Result:** The test passed with the existing implementation, so no additional implementation change was necessary.

## Cycle 4 — Alphabetical Tie-Breaking

- **RED:** Added a test to verify alphabetical ordering when books have equal borrowing counts.
- **RED commit:** `9f210e0`
- **GREEN:** Updated the sorting logic to use borrowing count and alphabetical title order.
- **GREEN commit:** `3c29900`
- **Result:** All four feature tests passed.
- **Regression testing:** The complete test suite passed with 59 tests.

## Cycle 5 — Never-Borrowed Books

- **Test:** Added a test containing borrowed and never-borrowed books.
- **Commit:** `9eadc5e`
- **Result:** The test passed with the existing implementation. Never-borrowed books were correctly sorted alphabetically.

## Reflection

This lab helped me understand Test-Driven Development and the importance of writing tests before implementation. I practiced the Red-Green approach by creating failing tests and then implementing the required functionality. I also learned how to use small Git commits to track changes throughout development. The tests helped verify empty catalogs, single books, popularity ordering, alphabetical tie-breaking, and never-borrowed books. Overall, I gained practical experience in writing tests, fixing issues, and checking that existing functionality continues to work.