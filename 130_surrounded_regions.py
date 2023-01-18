def solve(board):
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def dfs(row, col):
        board[row][col] = 'A'

        for dx, dy in displacements:
            new_row, new_col = row + dy, col + dx

            if 0 <= new_row < len(board) and 0 <= new_col < len(
                    board[0]) and board[new_row][new_col] == 'O':
                dfs(new_row, new_col)

    for row in range(len(board)):
        if board[row][0] == 'O':
            dfs(row, 0)

        if board[row][len(board[0]) - 1] == 'O':
            dfs(row, len(board[0]) - 1)

    for col in range(len(board[0])):
        if board[0][col] == 'O':
            dfs(0, col)

        if board[len(board) - 1][col] == 'O':
            dfs(len(board) - 1, col)

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'O':
                board[row][col] = 'X'
            elif board[row][col] == 'A':
                board[row][col] = 'O'

    return board


print(
    solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"],
           ["X", "O", "X", "X"]]))
