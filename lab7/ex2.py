import csv


def read_students_in_dictionary():
    students_dictionary = {}
    header = None

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


if __name__ == '__main__':
    students_dictionary, header = read_students_in_dictionary()

    print(header)

    students_dictionary = sort_students_dictionary(students_dictionary)
    for student in sort_students_dictionary(students_dictionary):
        print(students_dictionary[student])
