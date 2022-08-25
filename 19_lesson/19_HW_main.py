# ------------------------------------- Task_1 --------------------------------------

def with_index(word, start=1):
    indx = 0
    while start <= len(word):
        yield start, word[indx]
        start += 1
        indx += 1


# ------------------------------------- Task_2 --------------------------------------

def in_range(start=0, stop=0, step=1):
    value = start
    while value <= stop:
        yield value
        value += step


# ------------------------------------- Task_3 --------------------------------------


def main():

    # Task_1
    custom_enumerate = with_index('Hello', 1)
    for it_idx in custom_enumerate:
        print(it_idx)

    # Task_2
    custom_range = in_range(1, 10, 2)
    for num in custom_range:
        print(num)

    # Task_3


if __name__ == '__main__':
    main()
