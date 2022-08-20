from decorator import box_2
from functools import wraps
from time import time

def box(function):

    def wrapper():
        result = function()
        print('*' * len(result))
        print(result)
        print('*' * len(result))

    return wrapper

def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        before = time()
        result = function(*args, **kwargs)
        after = time()
        ex_time = after - before
        print(f'{function.__name__} was executed in {ex_time} seconds')

        return result

    return wrapper


@timer
def waste_some_time(number_of_time):
    for _ in range(number_of_time):
        sum (i ** 2 for i in range(10))

@box
def text():
    return 'Hello World'
@box
def text2():
    return 'Hello Dmytro'

@box_2
def text3(name):
    return f'Hello {name}'

def main():
    text()
    text2()
    text3('SV')
    waste_some_time(1)


if __name__ == '__main__':
    main()
