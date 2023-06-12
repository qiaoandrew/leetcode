def unique_paths(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for row_idx in range(1, m):
        for col_idx in range(1, n):
            dp[row_idx][col_idx] = dp[row_idx - 1][col_idx] + \
                dp[row_idx][col_idx - 1]
    return dp[-1][-1]


def unique_paths_optimized(m, n):
    dp = [[1 for _ in range(n)] for _ in range(2)]
    for row_idx in range(1, m):
        for col_idx in range(1, n):
            dp[1][col_idx] = dp[1][col_idx - 1] + dp[0][col_idx]
        for col_idx in range(n):
            dp[0][col_idx] = dp[1][col_idx]
            dp[1][col_idx] = 1
    return dp[0][-1]
