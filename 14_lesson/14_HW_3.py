def arg_rules(arg_1, arg_2, arg_3):

    def decorator(func):

        def wrapper(name):
            pattern = func(name)
            count_1, count_2 = 0, 0

            if isinstance(pattern, arg_1):
                pass
            else:
                print('Not str')

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


def main():
    print(create_slogan('S@SH05'))


if __name__ == '__main__':
    main()
