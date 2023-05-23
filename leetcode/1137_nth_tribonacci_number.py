class Solution:

    def tribonacci(self, n):
        tribonaccis = [0, 1, 1]

        if n <= 2:
            return tribonaccis[n]

        for _ in range(3, n + 1):
            tribonaccis = [tribonaccis[1], tribonaccis[2], sum(tribonaccis)]

        return tribonaccis[-1]