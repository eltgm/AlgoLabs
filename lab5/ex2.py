import csv


def get_students(file_name):
    students = []

    with open(file_name, encoding='utf8') as students_file:
        students_reader = csv.reader(students_file, delimiter=';')
        header = next(students_reader)
        print(header)
        for student_line in students_reader:
            students.append(student_line)

    return students


if __name__ == '__main__':
    students = sorted(get_students('students.csv'), key=lambda student_value: student_value[2])

    for student in students:
        print(student)
