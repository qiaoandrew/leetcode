def max_area_of_island(grid):
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    res = 0

    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(
                grid[0]) or grid[row][col] != 1:
            return 0

        grid[row][col] = 0

        area = 1

        for dx, dy in displacements:
            area += dfs(row + dy, col + dx)

        return area

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                res = max(res, dfs(row, col))

    return res


print(
    max_area_of_island([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
