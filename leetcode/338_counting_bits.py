class PopCountSolution:
    def count_bits(n):
        def pop_count(x):
            count = 0
            while x != 0:
                x &= x - 1
                count += 1
            return count
        
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
            
        return ans

class DP_Solution:
    def count_bits(n):
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp