def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for row in range(len(board)):
        for col in range(len(board[0])):
            val = board[row][col]

            if val == '.':
                continue

            box = row // 3 * 3 + col // 3

            if val in rows[row] or val in cols[col] or val in boxes[box]:
                return False

            rows[row].add(val)
            cols[col].add(val)
            boxes[box].add(val)

    return True


print(
    is_valid_sudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
