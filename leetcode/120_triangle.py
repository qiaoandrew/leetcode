def minimum_total(triangle):
    dp = [[0 for _ in range(row + 1)] for row in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for row in range(1, len(triangle)):
        for col in range(len(triangle[row])):
            cur = triangle[row][col]
            dp[row][col] = float('inf')
            if col > 0:
                dp[row][col] = min(dp[row][col], dp[row - 1][col - 1] + cur)
            if col < len(triangle[row - 1]):
                dp[row][col] = min(dp[row][col], dp[row - 1][col] + cur)
    return min(dp[-1])