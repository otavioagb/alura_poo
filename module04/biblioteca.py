from livro import Livro

book_one = Livro('1984', 'George Orwell', 1949)
book_two = Livro('O Poder Do Hábito', 'Charles Duhhig', 2012)
# for book in Livro.books:
#     print(book)
book_one.land()
available = Livro.check_availability(2012)
print(available)
