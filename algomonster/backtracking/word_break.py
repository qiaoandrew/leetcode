def word_break(s, words):
    def dfs(start_idx):
        if start_idx == len(s):
            return True
        
        if start_idx in memo:
            return memo[start_idx]

        ans = False
        for word in words:
            if s[start_idx:].startswith(word) and dfs(start_idx + len(word)):
                ans = True
                break

        memo[start_idx] = ans
        return ans

    memo = {}
    return dfs(0)

print(word_break('algomonster', ['algo', 'monster']))
print(word_break('aab', ['a', 'c']))