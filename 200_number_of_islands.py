def num_islands(grid):
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(
                grid[0]) or grid[row][col] != '1':
            return

        grid[row][col] = '0'

        for dx, dy in displacements:
            dfs(row + dy, col + dx)

    res = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                res += 1

                dfs(row, col)

    return res


print(
    num_islands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
                 ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
