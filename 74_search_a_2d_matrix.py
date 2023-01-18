def search_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        cur = matrix[row][col]

        if cur == target:
            return True
        elif cur < target:
            row += 1
        else:
            col -= 1

    return False


print(search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
