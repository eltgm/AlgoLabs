import csv


def get_students(file_name):
    students = []

    with open(file_name, encoding='utf8') as students_file:
        students_reader = csv.reader(students_file, delimiter=';')
        header = next(students_reader)

        for student_line in students_reader:
            students.append(student_line)

    return students, header


def subtract_students_ages(students):
    for student in students:
        student[2] = int(student[2]) - 1


def save_students(students):
    with open('students.csv', "w", newline="", encoding='utf8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(students)


if __name__ == '__main__':
    students, header = get_students('students.csv')
    students = sorted(students, key=lambda student_value: student_value[2])

    while True:
        print(header)
        for student in students:
            print(student)
        command = input('\nEnter command - ')

        if command == 'q':
            print('See you!')
            break
        elif command == 'subtract':
            subtract_students_ages(students)
            print('Subtract all ages by 1\n')
        elif command == 's':
            save_students(students)
            print('File saved!')
        else:
            print('Unrecognized command!\n')
