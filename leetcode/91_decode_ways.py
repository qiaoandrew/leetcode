def numDecodings(self, s: str) -> int:
    if s[0] == '0':
        return 0
    
    def can_decode(s):
        if s[0] == '0':
            return False
        return 1 <= int(s) <= 26
    
    dp = [1] * (len(s) + 1)
    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] if can_decode(s[i - 1]) else 0
        if i > 1:
            dp[i] += dp[i - 2] if can_decode(s[i - 2:i]) else 0
    
    return dp[-1]