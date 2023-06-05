from collections import deque

displacements = [(1, 2), (2, 1), (-1, -2), (-2, -1),
                 (1, -2), (2, -1), (-1, 2), (-2, 1)]


def get_knight_shortest_path(x, y):
    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    length = 0

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            if row == y and col == x:
                return length
            for dx, dy in displacements:
                new_row = row + dy
                new_col = col + dx

                if (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
        length += 1

    return length
