def subtract_if_bigger_than_22(students_dict):
    for student_id in range(1, len(students_dict)):
        student = students_dict[str(student_id)]

        student_age = int(student[1])
        if student_age > 22:
            student[1] = str(student_age - 1)


def print_students_with_even_ages(students_dict):
    students_dict_odd_age = {'№': students_dict['№']}
    for student_id in range(1, len(students_dict)):
        student = students_dict[str(student_id)]

        student_age = int(student[1])
        if student_age % 2 == 0:
            students_dict_odd_age[str(student_id)] = students_dict[str(student_id)]

    print_students(students_dict_odd_age)


def print_students(students_dict):
    for student in students_dict:
        print(students_dict[student])
    print('\n')


if __name__ == '__main__':
    students_list = [['№', 'ФИО', 'Возраст', 'Группа'],
                     ['4', 'Султаняров Владислав Алекссевич', '22', 'БО-111111'],
                     ['1', 'Иванов Иван Иванович', '23', 'БО-111111'],
                     ['2', 'Сидоров Семён Семёнович', '23', 'БО-111111'],
                     ['3', 'Яшков Илья Петрович', '24', 'БО-222222']
                     ]
    students_dict = {}

    for student in students_list:
        students_dict[student[0]] = list(student[1::])

    while True:
        print_students(students_dict)

        command = input('Enter command - ')

        if command == 'q':
            print('See you!')
            break
        elif command == 's':
            subtract_if_bigger_than_22(students_dict)
            print('Subtracted ages which bigger than 22 by 1\n')
        elif command == 'p':
            print_students_with_even_ages(students_dict)
            print('Printed all students which age is even')
        else:
            print('Unrecognized command!\n')
