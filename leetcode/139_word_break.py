def word_break(s, word_dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(dp)):
        for word in word_dict:
            if i >= len(word):
                if dp[i - len(word)] and s[i - len(word) : i] == word:
                    dp[i] = True

    return dp[-1]