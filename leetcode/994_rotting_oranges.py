from collections import deque


def oranges_rotting(grid):
    queue = deque()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                queue.append((row, col))

    minutes = 0

    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            for dx, dy in displacements:
                new_row, new_col = row + dy, col + dx

                if 0 <= new_row < len(grid) and 0 <= new_col < len(
                        grid[0]) and grid[new_row][new_col] == 1:
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 2

        minutes += 1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                return -1

    return minutes - 1 if minutes > 0 else 0


print(oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
print(oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
print(oranges_rotting([[0, 2]]))
