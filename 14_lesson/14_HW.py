"""Test new commit"""
# ------------------------------------- Task_1 --------------------------------------


def logger(func):

    def wrapper(*args):
        result = func(*args)
        print(result)

    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

# ------------------------------------- Task_2 --------------------------------------


def stop_words(words):

    def decorator(func):

        def wrapper(name):
            pattern = func(name)
            for word in words:
                pattern = pattern.replace(word, '*')

            return pattern

        return wrapper

    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f'{name} drinks pepsi in his brand new BMW!'

# ------------------------------------- Task_3 --------------------------------------


def arg_rules(arg_1, arg_2, arg_3):

    def decorator(func):

        def wrapper(name):
            pattern = func(name)
            count_1, count_2 = 0, 0

            if isinstance(pattern, arg_1):
                pass
            else:
                print('Not str')

            if len(pattern) > arg_2:
                print('Max length 15')

            for word in arg_3[0]:
                for i in pattern:
                    if i == word:
                        count_1 += 1
            for word in arg_3[1]:
                for i in pattern:
                    if i == word:
                        count_2 += 1

            if count_1 >= 1 and count_2 >= 1:
                pass
            else:
                print(f'Not found this: {arg_3} words.')

            return pattern

        return wrapper

    return decorator


@arg_rules(str, 15, ['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


@arg_rules(str, 50, ['05', '@'])
def create_slogan_2(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


def main():
    # Task_1
    add(4, 5)
    square_all(4, 5)

    # Task_2
    print(create_slogan("Steve"))

    # Task_3
    create_slogan('S@SH05')


if __name__ == '__main__':
    main()