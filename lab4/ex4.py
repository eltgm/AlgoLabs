if __name__ == '__main__':
    my_len = [['БО - 331101', ['Акулова Алена', 'Бабушкина Ксения']],
              ['БОВ - 421102', ['Петров Семен', 'Романов Станислав']],
              ['БО - 331103', ['Иванов Иван', 'Петров Всеволод']]]

    for group in my_len:
        for student in group[1]:
            second_name = student.split(' ')

            if len(second_name[0]) <= 7:
                print('{} группа - {}'.format(second_name, group[0]))
