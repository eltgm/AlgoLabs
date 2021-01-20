if __name__ == '__main__':
    my_len = [['БО - 331101', ['Акулова Алена', 'Бабушкина Ксения']],
              ['БОВ - 421102', ['Петров Семен', 'Романов Станислав']],
              ['БО - 331103', ['Иванов Иван', 'Петров Всеволод']]]

    group_name = input('Enter group - ')

    for group in my_len:
        if group[0] == group_name:
            print(group[0] + ': ' + ', '.join(group[1::1][0]))
