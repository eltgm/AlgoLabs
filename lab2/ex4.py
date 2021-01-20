if __name__ == '__main__':
    test_string = "213Hello, 219world 1! 1234"

    new_string = ''
    for i in range(len(test_string)):
        if not test_string[i].isdigit():
            new_string += test_string[i]

    print(new_string)
