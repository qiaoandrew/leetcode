class ExpandFromMiddleSolution:
    def longest_palindrome(s):
        res = ''
        res_len = 0

        for i in range(len(s)):
            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > res_len:
                    res_len = end - start + 1
                    res = s[start:end + 1]
                start -= 1
                end += 1

            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > res_len:
                    res_len = end - start + 1
                    res = s[start:end + 1]
                start -= 1
                end += 1

        return res

class DPSolution:
    def longest_palindrome(s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]
        
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
        
        i, j = ans
        return s[i:j + 1]