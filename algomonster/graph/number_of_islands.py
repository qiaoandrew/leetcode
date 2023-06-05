displacements = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def count_number_of_islands(grid):
    def dfs(row, col):
        grid[row][col] = 0
        visited.add((row, col))

        for dx, dy in displacements:
            new_row, new_col = row + dy, col + dx

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                dfs(new_row, new_col)

    visited = set()
    num_islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                num_islands += 1
                dfs(row, col)

    return num_islands
