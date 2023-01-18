def pacific_atlantic(heights):
    displacements = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    pacific = set()
    atlantic = set()

    def dfs(row, col, ocean):
        ocean.add((row, col))

        for dx, dy in displacements:
            new_row, new_col = row + dy, col + dx

            if 0 <= new_row < len(heights) and 0 <= new_col < len(
                    heights[0]) and heights[new_row][new_col] >= heights[row][
                        col] and (new_row, new_col) not in ocean:
                dfs(new_row, new_col, ocean)

    for row in range(len(heights)):
        dfs(row, 0, pacific)
        dfs(row, len(heights[0]) - 1, atlantic)

    for col in range(len(heights[0])):
        dfs(0, col, pacific)
        dfs(len(heights) - 1, col, atlantic)

    res = []

    for row in range(len(heights)):
        for col in range(len(heights[0])):
            if (row, col) in pacific and (row, col) in atlantic:
                res.append([row, col])

    return res


print(
    pacific_atlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1],
                      [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
