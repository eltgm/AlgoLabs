def create_table(students_data):
    student_data_21 = list(filter(lambda student_data: student_data[1] == '21 год', students_data))
    student_data_21.insert(0, students_data[0])

    student_with_max_name = student_data_21[0]
    for student in student_data_21:
        if len(student[0]) > len(student_with_max_name[0]):
            student_with_max_name = student

    is_first_row = True

    for student in student_data_21:
        if is_first_row:
            print('{}\t\t\t\t\t\t\t\t{}\t\t{}'.format(student[0], student[1], student[2]))
            is_first_row = False
            continue

        tabs = "\t\t" if len(student[0]) + 5 > len(student_with_max_name[0]) else "\t\t\t"

        print('{}{}{}\t\t{}'.format(student[0], tabs, student[1], student[2]))


if __name__ == '__main__':
    my_string = '''
    ФИО;Возраст;Категория;
    _Иванов Иван Иванович;23 года;Студент 3 курса;
    _Петров Семен Игоревич;22 года;Студент 2 курса;
    _Иванов Семен Игоревич;22 года;Студент 2 курса;
    _Акибов Ярослав Наумович;23 года;Студент 3 курса;
    _Борков Станислав Максимович;21 год;Студент 1 курса;
    _Петров Семен Семенович;21 год;Студент 1 курса;
    _Романов Станислав Андреевич;23 года;Студент 3 курса;
    _Петров Всеволод Борисович;21 год;Студент 2 курса
    '''

    students = my_string.replace("\n", "").split("_")

    students_data = []
    for student in students:
        student_data = student.strip().split(';')
        students_data.append(student_data)
    create_table(students_data)
