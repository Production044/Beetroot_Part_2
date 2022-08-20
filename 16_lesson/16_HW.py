# ------------------------------------- Task_1 --------------------------------------

class People():

    def __init__(self, name):
        self.name = name


class Teacher(People):

    def __init__(self, name, group, selary, teacher_name):
        super().__init__(name)
        self.selary = selary
        self.group = group
        self.teacher_name = teacher_name

    def start_lesson(self):
        print(f'Lesson open for {self.group}\n'
              f'Teacher: {self.teacher_name}')

    def stop_lesson(self):
        print(f'Lesson close for {self.group}\n'
              f'{self.teacher_name} earned {self.selary} BTC')


class Student(People):

    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def start_learning(self):
        print(f'Students {self.name} from {self.group} started studying')

    def stop_learning(self):
        print(f'Students {self.name} from {self.group} stopped studying')


# ------------------------------------- Task_2 --------------------------------------

class Mathematician:

    def square_nums(self, list):
        return print([i ** 2 for i in list])

    def remove_positives(self, list):
        return print([i for i in list if i <0])

    def filter_leaps(self, list):
        return print([i for i in list if i % 4 == 0])


def main():

    # Task 1
    students = 'Dmytro, Svitlana, Oksana'
    group_list = ['11-A', '11-B', '11-C']
    student = Student(students, group_list[0])
    teacher = Teacher(students, group_list[0], 1000, 'Amanda')
    teacher.start_lesson()
    student.start_learning()
    teacher.stop_lesson()
    print()

    # Task 2
    m = Mathematician()
    m.square_nums([7, 11, 5, 4])
    m.remove_positives([26, -11, -8, 13, -90])
    m.filter_leaps([2001, 1884, 1995, 2003, 2020])


if __name__ == '__main__':
    main()