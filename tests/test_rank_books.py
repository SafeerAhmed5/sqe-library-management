import libraryhub.library as library_module
from libraryhub.library import Library


# Cycle 1: Empty catalog
def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()
    assert library_module.rank_books_by_popularity(library) == []


# Cycle 2: Single book
def test_rank_books_returns_single_book():
    library = Library()
    book = library_module.Book("Python Basics", 5)
    library.add_book(book)

    result = library_module.rank_books_by_popularity(library)
    assert result == [book]


# Cycle 3: Multiple books
def test_rank_books_sorted_by_borrow_count():
    library = Library()

    book1 = library_module.Book("Python", 2)
    book2 = library_module.Book("Java", 8)
    book3 = library_module.Book("C++", 5)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    result = library_module.rank_books_by_popularity(library)
    assert result == [book2, book3, book1]


# Cycle 4: Alphabetical tie-breaking
def test_rank_books_tie_breaks_alphabetically():
    library = Library()

    book1 = library_module.Book("Python", 5)
    book2 = library_module.Book("C++", 5)
    book3 = library_module.Book("Java", 8)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    result = library_module.rank_books_by_popularity(library)
    assert result == [book3, book2, book1]