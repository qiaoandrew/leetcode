import math


def perfect_squares(n):
    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0
    for root in range(1, int(math.sqrt(n)) + 1):
        num = root ** 2
        for dp_num in range(1, n + 1):
            if dp_num >= num:
                dp[dp_num] = min(dp[dp_num], dp[dp_num - num] + 1)
    return dp[n]
