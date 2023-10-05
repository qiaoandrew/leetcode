def count_palindromes(s):
    res = 0
    for i in range(len(s)):
        start, end = i, i
        while start >= 0 and end < len(s) and s[start] == s[end]:
            res += 1
            start -= 1
            end += 1
        
        start, end = i, i + 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            res += 1
            start -= 1
            end += 1
    return res

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
            count += 1
        
        for i in range(len(s) - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            count += dp[i][i + 1]
        
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                count += dp[i][j]
        
        return count