class Livro:
    
    books = []

    def __init__(self, title='', author='', published_year=0):
        self.title = title
        self.author = author
        self.published_year = published_year
        self.available = True
        Livro.books.append(self)

    def __str__(self):
        published_year = str(self.published_year)
        # print('')
        return f' {self.title.ljust(25)} | {self.author.ljust(25)} | {published_year.ljust(6)}'
    
    def land(self):
        self.available = False

    @staticmethod
    def check_availability(published_year):
        for book in Livro.books:
            if book.published_year == published_year and book.available:
                available_books = book
                return available_books
            else:
                return 'No books available for this year'