# ------------------------------------- Task_1 --------------------------------------
import re
from functools import wraps

class Validator:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, check_email):
        not_valid_word = "^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"

        if not re.search(not_valid_word, check_email):
            raise ValueError('Your email on not Valid')

        self._email = check_email
        print(check_email)

# ------------------------------------- Task_2 --------------------------------------


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self._id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    @property
    def workers(self):
        return self.workers

    @workers.setter
    def workers(self, value):
        self._workers = value

    def __str__(self):
        return f'ID: {self._id}, Boss name: {self._name}, ' \
               f'Company: {self._company}, Worker: {self._workers}'


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self._id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def id_(self):
        return self._id

    @id_.setter
    def id_(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    def __str__(self):
        return f'ID: {self._id}, Worker name: {self._name}, ' \
               f'Company: {self._company}, Boss: {self.boss.name}'


# ------------------------------------- Task_3 --------------------------------------

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return int(func(*args, **kwargs))
            except ValueError:
                return 'function is not convertable'
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return str(func(*args, **kwargs))
            except ValueError:
                return 'function is not convertable'
        return wrapper

    @staticmethod
    def to_boll(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return bool(func(*args, **kwargs))
            except ValueError:
                return 'function is not convertable'
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return float(func(*args, **kwargs))
            except ValueError:
                return 'function is not convertable'
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_boll
def do_something(string: str):
    return string


@TypeDecorators.to_float
def do_anything(string: str):
    return string


def main():

    # Task_1

    validate = Validator('dmitry.klimenko.work@gmail.com')

    # Task_2

    boss = Boss(1, 'Richard Branson', 'Virgin Galactic')
    workers1 = Worker(2, 'David', boss.company, boss)
    workers2 = Worker(3, 'Steve', boss.company, boss)
    print(boss, workers1, workers2, sep='\n')

    # Task_3

    print(type(do_nothing('30')))
    print(type(do_something('30')))
    print(type(do_anything('30')))


if __name__ == '__main__':
    main()
