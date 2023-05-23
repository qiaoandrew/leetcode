from collections import deque


# bfs using queue for tiles and steps so far and visited set
# function to get row and col based on tile number
def snakes_and_ladders(board):

    def get_position(tile):
        row = (tile - 1) // len(board)
        col = (tile - 1) % len(board)

        if row % 2 == 0:
            return (len(board) - row - 1, col)
        else:
            return (len(board) - row - 1, len(board) - col - 1)

    # (tile, steps)
    queue = deque([(1, 0)])
    visited = {1}

    while queue:
        tile, steps = queue.popleft()

        row, col = get_position(tile)

        if board[row][col] != -1:
            tile = board[row][col]

        if tile == len(board)**2:
            return steps

        for move in range(1, 7):
            new_tile = tile + move

            if new_tile not in visited and new_tile <= len(board)**2:
                visited.add(new_tile)
                queue.append((new_tile, steps + 1))

    return -1


# bfs
# function to get row and col based on tile number
# def snakes_and_ladders(board):

#     def get_position(tile):
#         row = (tile - 1) // len(board)
#         col = (tile - 1) % len(board)

#         if row % 2 == 0:
#             return (len(board) - row - 1, col)
#         else:
#             return (len(board) - row - 1, len(board) - col - 1)

#     # cell, steps
#     queue = deque([(1, 0)])
#     visited = {1}

#     while queue:
#         tile, steps = queue.popleft()

#         row, col = get_position(tile)

#         if board[row][col] != -1:
#             tile = board[row][col]

#         if tile == len(board) * len(board):
#             return steps

#         for move in range(1, 7):
#             new_tile = tile + move

#             if new_tile not in visited and new_tile <= len(board) * len(board):
#                 visited.add(new_tile)
#                 queue.append((new_tile, steps + 1))

#     return -1