def word_break(s, word_dict):
    dp = {i: False for i in range(len(s))}

    for i in range(len(s)):
        for word in word_dict:
            if i >= len(word) - 1 and \
            (i == len(word) - 1 or dp[i - len(word)]) and \
            s[i - len(word) + 1:i + 1] == word:
                dp[i] = True

    return dp[len(s) - 1]