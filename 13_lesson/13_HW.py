# ------------------------------------- Task_1 --------------------------------------

def foo():
    a = 1
    b = 2
    с = 3
    d = 4

# ------------------------------------- Task_2 --------------------------------------


def total_cost(people):
    def total_people(cost):
        return people * cost
    return total_people


def main():
    # Task_1
    print(foo.__code__.co_nlocals)

    # Task_2
    total = total_cost(int(input('Кількість військових: ')))
    print(f'Загальні витрати: {total(int(input("Витрати на одного війскового: ")))} грн.')


if __name__ == '__main__':
    main()
