from src.Author import Author
from src.ISBNValidator import ISBNValidator


class Book:
    def __init__(self, title, author, ISBN) -> None:
        validator = ISBNValidator()
        if not isinstance(title, str):
            raise TypeError("Title must be string")
        if not isinstance(author, Author):
            raise TypeError("Author must be of class actor")
        if not validator.validate(ISBN):
            raise TypeError("ISBN must be valid ISBN-13 number")
        self.title = title
        self.author = author
        self.ISBN = ISBN
