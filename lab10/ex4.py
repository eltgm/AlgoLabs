if __name__ == '__main__':
    matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
              [8, 7, 6, 5, 4, 3, 2, 1],
              [2, 3, 4, 5, 6, 7, 8, 9],
              [9, 8, 7, 6, 5, 4, 3, 2],
              [1, 3, 5, 7, 9, 7, 5, 3],
              [3, 1, 5, 3, 2, 6, 5, 7],
              [1, 7, 5, 9, 7, 3, 1, 5],
              [2, 6, 3, 5, 1, 7, 3, 2]]

    for row in matrix:
        temp = row[0]
        row[0] = row[len(row) - 1]
        row[len(row) - 1] = temp

    for row in matrix:
        print(row)
