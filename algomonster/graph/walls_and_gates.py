from collections import deque

displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def map_gate_distances(dungeon_map):
    rows, cols = len(dungeon_map), len(dungeon_map[0])
    queue = deque()

    for row in range(rows):
        for col in range(cols):
            if dungeon_map[row][col] == 0:
                queue.append((row, col))

    distance_from_gate = 0
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            dungeon_map[row][col] = min(dungeon_map[row][col], distance_from_gate)

            for dx, dy in displacements:
                new_row, new_col = row + dy, col + dx

                if 0 <= new_row < rows and 0 <= new_col < cols and dungeon_map[new_row][new_col] == 2147483647:
                    queue.append((new_row, new_col))
        distance_from_gate += 1

    return dungeon_map