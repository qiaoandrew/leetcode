def longest_common_subsequence(text1, text2):
    dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
    for p1 in range(len(text1)):
        for p2 in range(len(text2)):
            if text1[p1] == text2[p2]:
                dp[p1 + 1][p2 + 1] = dp[p1][p2] + 1
            else:
                dp[p1 + 1][p2 + 1] = max(dp[p1][p2 + 1], dp[p1 + 1][p2])
    return dp[-1][-1]