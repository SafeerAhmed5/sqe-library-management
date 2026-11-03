import libraryhub.library as library_module
from libraryhub.library import Library


def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()

    assert library_module.rank_books_by_popularity(library) == []