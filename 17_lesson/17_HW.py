# ------------------------------------- Task_1 --------------------------------------

class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('Must be implemented by the sub class')


class Cat(Animal):

    def talk(self):
        print(f'Cat {self.name} say: Mey')


class Dog(Animal):

    def talk(self):
        print(f'Dog  {self.name} say: Gaff')


class Duck(Animal):

    def talk(self):
        print(f'Duck {self.name} say: Ga ga ga')

cat, dog, duck = Cat('Martin'), Dog('Bethoven'), Duck('Ducky')
animals = [cat, dog, duck]


def animal_voice():

    for animal in animals:
        print(animal.talk())

# ------------------------------------- Task_2 --------------------------------------


class Author:
    def __init__(self, name, country, birthday, books: list):
        self.name_author = name
        self.country_author = country
        self.birthday_author = birthday
        self.books_author = books

    def __str__(self):
        return f'Author: {self.name_author}, {self.country_author},' \
               f'{self.birthday_author}, {self.books_author}'

    def __repr__(self):
        return self.__str__()


class Book:
    numbers_books = 0

    def __init__(self, name, year, author: Author):
        self.name_book = name
        self.year_book = year
        self.author_book = author
        Book.numbers_books += 1

    def __str__(self):
        return f' {self.name_book} written in {self.year_book}' \
               f' author {self. author_book.name_author}'

    def __repr__(self):
        return self.__str__()


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
        self.book = None
        self.author = None

    def new_book(self, book: Book):
        self.book = book
        self.books.append(book)
        if book.author_book not in self.authors:
            self.authors.append(book.author_book)

    def group_by_author(self, author_name):
        for author in self.authors:
            if author_name == author.name_author:
                print(author.books)

    def group_by_year(self, book_year):
        books_list_by_year = []
        for book in self.books:
            if book_year == book.year_book:
                books_list_by_year.append(book)
        return books_list_by_year



def main():

    # Task 1
    animal_voice()

    # Task 2
    lib = Library('UA')
    lst1 = ["Harry Potter series", "The Ickabog", "Fantastic Beasts and Where to Find Them"]
    lst2 = ["A Song of Ice and Fire", "Knight of the Seven Kingdoms", "Dying of the Light"]
    Joanne_Rowling = Author('J. K. Rowling', 'Great Britain', '07.31.1965', lst1)
    George_Martin = Author('George R. R. Martin', 'U.S.A.', '09.20.1948', lst2)
    book1 = Book('Harry Potter and the Philosopher\'s Stone', '1997', Joanne_Rowling)
    book2 = Book('A Game of Thrones', 1999, George_Martin)
    print(book1)
    print(book2)
    lib.new_book(book1)
    lib.new_book(book2)
    lib.group_by_author(George_Martin)
    lib.group_by_year(1999)
    print(lib)


if __name__ == '__main__':
    main()
