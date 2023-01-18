from collections import deque


def walls_and_gates(rooms):
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    queue = deque()

    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                queue.append((row, col))

    distance = 0

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()

            if rooms[row][col] == 2147483647:
                rooms[row][col] = distance

            for dx, dy in displacements:
                new_row, new_col = row + dy, col + dx

                if 0 <= new_row < len(rooms) and 0 <= new_col < len(
                        rooms[0]) and rooms[new_row][new_col] == 2147483647:
                    queue.append((new_row, new_col))

        distance += 1

    return rooms