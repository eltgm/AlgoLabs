import random


# Sum of items in range by 0 to 10
def sum():
    test_values = [random.random() * 20 for i in range(random.randint(1, 10))]
    print(test_values)

    test_values_sum = 0
    for item in test_values:
        if 0 < item < 10:
            test_values_sum += item

    print(test_values_sum)


# Slice list to only odd items
def odd_items():
    test_values = ["test1", 2, "test3", "test4", 5, 6, 7, "test8", "test9", 10]

    for item in test_values[0::2]:
        print(item)


# Calculate functions
def read_variable(variable_name):
    while True:
        variable = input("{} = ".format(variable_name))

        if variable.isdigit():
            return float(variable)


def calculate():
    a = read_variable("a")
    b = read_variable("b")
    c = read_variable("c")
    d = read_variable("d")
    k = read_variable("k")

    try:
        return abs((a ** 2 - b ** 3 - c ** 3 * a ** 2) * (b - c + c * (k - d / (b ** 3))) - (
                (k / b - k / a) * c) ** 2 - 20000)
    except ZeroDivisionError:
        return "Division by zero!"


if __name__ == '__main__':
    while True:
        print('''
0 - Выход из программы
1 - Вычисление заданной функции
2 - Вывод четных элементов list
3 - Сумма элементов в диапозоне от 0 до 10
    ''')

        function = input('Выберите функцию - ')

        if function == '0':
            print('Выход...')
            break
        elif function == '1':
            print('Выполняем функцию 1...')
            print(calculate())
        elif function == '2':
            print('Выполняем функцию 2...')
            odd_items()
        elif function == '3':
            print('Выполняем функцию 3...')
            sum()

        answer = input('Вы хотите продолжить? ')

        if not (answer == 'Y' or answer == 'yes' or answer == '1'):
            print('Выход...')
            break
