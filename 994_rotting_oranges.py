from collections import deque


def oranges_rotting(grid):
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    rotten_oranges = deque()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                rotten_oranges.append((row, col))

    res = 0

    while rotten_oranges:
        for _ in range(len(rotten_oranges)):
            row, col = rotten_oranges.popleft()

            for dx, dy in displacements:
                new_row, new_col = row + dy, col + dx

                if 0 <= new_row < len(grid) and 0 <= new_col < len(
                        grid[0]) and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    rotten_oranges.append((new_row, new_col))

        res += 1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return -1

    return res - 1 if res > 0 else 0


print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(oranges_rotting([[0, 2]]))
