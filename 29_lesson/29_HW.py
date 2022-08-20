# ------------------------------------- Task_1 --------------------------------------

def binary_search_recursive(list, index_0, index_n, value_to_find):
    if index_n < index_0:
        return None
    else:
        middle_value = index_0 + ((index_n - index_0) // 2)

        if list[middle_value] > value_to_find:
            return binary_search_recursive(list, index_0, middle_value - 1, value_to_find)
        elif list[middle_value] < value_to_find:
            return binary_search_recursive(list, middle_value + 1, index_n, value_to_find)
        else:
            return middle_value

# ------------------------------------- Task_2 --------------------------------------


def find_fibonacci_element(n):
    fib_1 = 1
    fib_2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = fib_sum
        i = i + 1
    return print("The value of this element:", fib_2)


def main():

    # Task_1
    print('Task 1:')
    list = [17, 10, 18, 46, 94, 142]
    print(f'Value: 94 in position: {binary_search_recursive(list, 0, len(list), 94)}')

    # Task_2
    print('Task 2:')
    find_fibonacci_element(int(input("Fibonacci string element number: ")))

    # Task_3


if __name__ == '__main__':
    main()
