def box_2(function):

    def wrapper(name):
        result = function(name)
        print('*' * len(result))
        print(result)
        print('*' * len(result))

    return wrapper