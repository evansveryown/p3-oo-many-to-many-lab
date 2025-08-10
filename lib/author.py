# lib/author.py
class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        from lib.contract import Contract
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        from lib.contract import Contract
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())
