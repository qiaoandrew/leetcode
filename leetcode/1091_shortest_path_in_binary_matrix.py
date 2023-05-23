from collections import deque


def shortest_path_binary_matrix(grid):
    n = len(grid)
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1),
                     (-1, 1), (1, -1)]

    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1

    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    length = 1

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if x == y == n - 1:
                return length

            for dx, dy in displacements:
                new_x = x + dx
                new_y = y + dy

                if (new_x, new_y) not in visited and \
                  0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
                    visited.add((new_x, new_y))

        length += 1

    return -1