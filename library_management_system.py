# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class LibraryManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            print("Title:", book.title, "| Author:", book.author)


# Program execution
library = LibraryManagementSystem()
library.add_book("Introduction to Python", "Guido van Rossum")
library.add_book("Software Engineering", "Ian Sommerville")
library.display_books()
