from collections import deque

displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def flood_fill(r, c, replacement, image):
    color_to_replace = image[r][c]
    queue = deque([(r, c)])
    visited = set([(r, c)])

    while queue:
        row, col = queue.popleft()
        image[row][col] = replacement

        for dx, dy in displacements:
            new_row, new_col = row + dy, col + dx

            if 0 <= new_row < len(image) and 0 <= new_col < len(image[0]) and not (new_row, new_col) in visited and image[new_row][new_col] == color_to_replace:
                queue.append((new_row, new_col))
                visited.add((new_row, new_col))

    return image
