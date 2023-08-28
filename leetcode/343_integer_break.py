class Solution:
    def integerBreak(self, n: int) -> int:
        if n in [2, 3]:
            return n - 1
        
        num_2 = [0, 2, 1][n % 3]
        num_3 = (n - num_2 * 2) // 3
        return 3 ** num_3 * 2 ** num_2