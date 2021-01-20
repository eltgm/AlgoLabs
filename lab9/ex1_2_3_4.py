def print_students(students_dict):
    for student in students_dict:
        print(student + " " + ';'.join(students_dict[student]))
    print('\n')


def save_student(students_dict, student_raw, is_update):
    update_index = 1 if is_update else 0

    student_id = str(len(students_dict) + 1) if not is_update else student_raw[0]
    student = [
        '{} {} {}'.format(student_raw[0 + update_index], student_raw[1 + update_index], student_raw[2 + update_index]),
        student_raw[3 + update_index], student_raw[4 + update_index]]

    students_dict[student_id] = student


if __name__ == '__main__':
    students_dict = {'№': ['ФИО', 'Возраст', 'Группа'],
                     '4': ['Султаняров Владислав Алекссевич', '22', 'БО-111111'],
                     '1': ['Иванов Иван Иванович', '23', 'БО-111111'],
                     '2': ['Сидоров Семён Семёнович', '23', 'БО-111111'],
                     '3': ['Яшков Илья Петрович', '24', 'БО-222222']}

    while True:
        command_with_params = input('Enter command - ')
        command_with_params_raw = command_with_params.split(' ')
        command = command_with_params_raw[0]

        if command == 'q':
            print('See you!')
            break
        elif command == 'g':
            student_id = command_with_params_raw[1]
            print(students_dict[student_id])
        elif command == 'a':

            save_student(students_dict, command_with_params_raw[1::], False)
            print('Student successfully added!')
        elif command == 'u':
            save_student(students_dict, command_with_params_raw[1::], True)
            print('Student successfully updated!')
        elif command == 'd':
            student_id = command_with_params_raw[1]

            del students_dict[student_id]
            print('Student successfully deleted!')
            print_students(students_dict)
        else:
            print('Unrecognized command!')
