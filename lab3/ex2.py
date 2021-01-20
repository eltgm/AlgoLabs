if __name__ == '__main__':
    my_string = '''Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'''

    students = my_string.split('_')

    is_first_row = True
    for student in students:
        student_data = student.split(';')
        if is_first_row:
            print('{}{}{}\t\t\t\t\t\t{}\t\t{}'.format(student_data[0], student_data[1], student_data[2],
                                                student_data[3], student_data[4]))
            is_first_row = False
            continue

        print('{} {} {}\t{}\t\t{}'.format(student_data[0], student_data[1], student_data[2],
                                            student_data[3], student_data[4]))
