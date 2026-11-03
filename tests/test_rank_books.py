import libraryhub.library as library_module
from libraryhub.library import Library


def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()

    assert library_module.rank_books_by_popularity(library) == []


def test_rank_books_returns_single_book():
    library = Library()
    book = library_module.Book("Python Basics", 5)
    library.add_book(book)

    result = library_module.rank_books_by_popularity(library)

    assert result == [book]