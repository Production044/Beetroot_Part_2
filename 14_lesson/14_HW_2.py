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


def main():
    print(create_slogan("Steve"))


if __name__ == '__main__':
    main()