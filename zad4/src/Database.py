class DatabaseError(Exception):
    pass


class Database:
    def __init__(self, books={}) -> None:
        self.books = books

    def api_call(self, *args):
        pass

    def get_books(self):
        return self.api_call("get", "books")

    def get_book(self, id):
        return self.api_call("get", f"books{id}")

    def add_book(self, book):
        return self.api_call("post", "books", book)

    def delete_book(self, id):
        return self.api_call("delete", f"books{id}")

    def edit_book(self, book):
        return self.api_call("put", f"books{book.ISBN}")
