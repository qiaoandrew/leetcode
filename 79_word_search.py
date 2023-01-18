# nested for loop through board, call dfs function on each
# set to keep track of (row, col) in current path
# dfs takes row, col, char index
# if index goes beyond word, all chars were found, return True
# if cell doesn't exist, char doesn't match or cell is already in path return False
# add (row, col) to path
# boolean exists = call dfs function on each neighbour
# remove (row, col) from path
# return exists
def exist(board, word):
    path = set()

    def dfs(row, col, i):
        if i == len(word):
            return True

        if row < 0 or row >= len(board) or col < 0 or col >= len(
                board[0]) or board[row][col] != word[i] or (row, col) in path:
            return False

        path.add((row, col))

        exists = dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or dfs(
            row, col + 1, i + 1) or dfs(row, col - 1, i + 1)

        path.remove((row, col))

        return exists

    for row in range(len(board)):
        for col in range(len(board[0])):
            if dfs(row, col, 0):
                return True

    return False
