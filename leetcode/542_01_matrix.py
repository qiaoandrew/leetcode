from collections import deque

def update_matrix(mat):
    rows, cols = len(mat), len(mat[0])
    nearest_zero = [[0] * cols for _ in range(rows)]

    queue = deque()
    visited = set()
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 0:
                queue.append((row, col))
                visited.add((row, col))
    
    cur_distance = 0
    displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            nearest_zero[row][col] = cur_distance

            for dx, dy in displacements:
                new_row, new_col = row + dy, col + dx
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        cur_distance += 1
    
    return nearest_zero