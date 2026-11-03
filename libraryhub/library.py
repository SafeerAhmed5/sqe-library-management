class Book:
    def __init__(self, title, times_borrowed=0):
        self.title = title
        self.times_borrowed = times_borrowed


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
