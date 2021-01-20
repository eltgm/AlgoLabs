if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    sum = 0
    for row in matrix:
        for element in row:
            sum += element

    print(sum)
