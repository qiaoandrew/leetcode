from collections import deque


# loop through and save all rooms with a gate
# bfs neighbours while incrementing distance from nearest gate
def walls_and_gates(rooms):
    queue = deque()

    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                queue.append((row, col))

    distance = 0

    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

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


print(
    walls_and_gates([[2147483647, -1, 0, 2147483647],
                     [2147483647, 2147483647, 2147483647, -1],
                     [2147483647, -1, 2147483647, -1],
                     [0, -1, 2147483647, 2147483647]]))
print(walls_and_gates([[-1]]))