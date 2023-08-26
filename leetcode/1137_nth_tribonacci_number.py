class Solution:
    def tribonacci(self, n: int) -> int:
        prev_3 = [0, 1, 1]
        
        if n <= 2:
            return prev_3[n]
        
        for _ in range(3, n + 1):
            prev_3 = [prev_3[1], prev_3[2], sum(prev_3)]
        
        return prev_3[-1]