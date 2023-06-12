def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for row_idx in range(1, rows):
        dp[row_idx][0] = dp[row_idx - 1][0] + grid[row_idx][0]
    for col_idx in range(1, cols):
        dp[0][col_idx] = dp[0][col_idx - 1] + grid[0][col_idx]
    for row_idx in range(1, rows):
        for col_idx in range(1, cols):
            dp[row_idx][col_idx] = min(
                dp[row_idx - 1][col_idx], dp[row_idx][col_idx - 1]) + grid[row_idx][col_idx]
    return dp[-1][-1]
