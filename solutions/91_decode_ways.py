# start from end and loop forwards
# no decodings if starting at 0
# otherwise start with the value at the next letter
# if current is 1 or 2, check if double number decoding is possible
def num_decodings(s):
    dp = {len(s): 1}

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]

        if i < len(s) - 1 and (s[i] == '1' or
                               (s[i] == '2' and s[i + 1] in '0123456')):
            dp[i] += dp[i + 2]

    return dp[0]
