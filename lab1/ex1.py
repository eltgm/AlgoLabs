def read_variable(variable_name):
    while True:
        variable = input("{} = ".format(variable_name))

        if variable.isdigit():
            return float(variable)


def calculate(a, b, c, d, k):
    try:
        return abs((a ** 2 - b ** 3 - c ** 3 * a ** 2) * (b - c + c * (k - d / (b ** 3))) - (
                (k / b - k / a) * c) ** 2 - 20000)
    except ZeroDivisionError:
        return "Division by zero!"


if __name__ == '__main__':
    a = read_variable("a")
    b = read_variable("b")
    c = read_variable("c")
    d = read_variable("d")
    k = read_variable("k")

    print(calculate(a, b, c, d, k))
