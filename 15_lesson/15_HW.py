# ------------------------------------- Task_1 --------------------------------------

class Person:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


def talk(name, surname, age):
    total_data = Person(name, surname, age)
    return print(f'Hello, my name is {total_data.name} {total_data.surname}'
                 f' and I’m {total_data.age} years old')

# ------------------------------------- Task_2 --------------------------------------

class Dog:

    age_factor = 7

    def __init__(self, age):
        self.age = age


def human_age(num):
    dog_age = num * Dog.age_factor

    return print(f'В перерахунку на собачий вік вашій собаці: {dog_age} років')

# ------------------------------------- Task_3 --------------------------------------


class TVController:
    chanels_list = ['FOX', 'BBC', 'SPORT']

    def first_chanel(self):
        print(self.chanels_list[0])

    def last_chanel(self):
        print(self.chanels_list[-1])

    def change_chanel(self, motion):
        if motion == 1:
            print(self.chanels_list[0])

        if motion == 2:
            print(self.chanels_list[1])

        if motion == 3:
            print(self.chanels_list[2])

        if motion == 0 and motion >= 4:
            print(self.chanels_list[0])


def main():

    # Task_1
    talk('Dmytro', 'Klymenko', '30')

    # Task_2

    human_age(int(input('Скільки вашій собаці років?\n'
                        'Відповідь: ')))

    # Task_3
    start_tv = TVController()
    start_tv.first_chanel()
    start_tv.change_chanel(3)


if __name__ == '__main__':
    main()