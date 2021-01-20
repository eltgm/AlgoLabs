import csv


def save_students(students, header):
    with open('students_new.csv', "w", newline="", encoding='utf8') as file:
        file.write(';'.join(header) + '\n')
        students_list = []
        for student_id in students:
            students_list.append(student_id + ';' + ';'.join(students[student_id]) + '\n')
        file.writelines(students_list)


def subtract_students_ages(students_dictionary):
    for student in students_dictionary:
        students_dictionary[student][1] = str(int(students_dictionary[student][1]) - 1)


def read_students_in_dictionary():
    students_dictionary = {}

    with open('students.csv') as students_file:
        students_reader = csv.reader(students_file, delimiter=';')
        header = next(students_reader)
        for row in students_reader:
            students_dictionary[row[0]] = list(row[1::])
    return students_dictionary, header


def sort_students_dictionary(students_dictionary):
    students_count = len(students_dictionary)

    for i in range(1, students_count):
        for j in range(i + 1, students_count + 1):
            if students_dictionary[str(i)][1] > students_dictionary[str(j)][1]:
                temp_student = students_dictionary[str(i)]
                students_dictionary[str(i)] = students_dictionary[str(j)]
                students_dictionary[str(j)] = temp_student

    return students_dictionary


def print_students(students_dictionary, header):
    print(header)
    for student in students_dictionary:
        print(students_dictionary[student])
    print('\n')


if __name__ == '__main__':
    students_dictionary, header = read_students_in_dictionary()

    students_dictionary = sort_students_dictionary(students_dictionary)

    while True:
        print_students(students_dictionary, header)

        command = input('Enter command - ')

        if command == 'q':
            print('See you!')
            break
        elif command == 'subtract':
            subtract_students_ages(students_dictionary)
            print('Subtract all ages by 1\n')
        elif command == 's':
            save_students(students_dictionary, header)
            print('File saved!')
        else:
            print('Unrecognized command!\n')
