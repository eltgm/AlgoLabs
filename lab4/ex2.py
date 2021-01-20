if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    new_list = test_list[::2]

    new_list.append('new element 1')
    new_list.append('new element 2')

    print(new_list)
