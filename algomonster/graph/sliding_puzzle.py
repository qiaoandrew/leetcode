from collections import deque

displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

target_pos = ((1, 2, 3), (4, 5, 0))


def num_steps(init_pos):
    init_pos = tuple(tuple(row) for row in init_pos)
    queue = deque([init_pos])
    visited = set([init_pos])
    steps = 0

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur == target_pos:
                return steps

            row, col = 0, 0
            for row_idx, values in enumerate(cur):
                for col_idx, value in enumerate(values):
                    if value == 0:
                        row, col = row_idx, col_idx

            for dx, dy in displacements:
                new_row, new_col = row + dy, col + dx

                if 0 <= new_row < 2 and 0 <= new_col < 3:
                    new = [list(row) for row in cur]
                    new[row][col], new[new_row][new_col] = new[new_row][new_col], new[row][col]
                    new_tuple = tuple(tuple(row) for row in new)

                    if new_tuple not in visited:
                        queue.append(new_tuple)
                        visited.add(new_tuple)

        steps += 1

    return -1
