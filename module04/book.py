class Book:
    
    books = []

    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self._available = True
        Book.books.append(self)

    def __str__(self):
        return f"Title: {self.title} | Author: {self.author} | Publication Year: {self.publication_year}\n"
    
    def borrow(self):
        self._available = False

    @classmethod
    def check_availability(cls, year):
        check = [book for book in cls.books if book.publication_year == year and book._available]
        if check:
            for book in check:
                print(book)
        return f'No books available in {year}.'
    
    @classmethod
    def all_books(cls):
        return "\n".join(str(book) for book in cls.books)