def decode_ways(digits):
    def dfs(start_idx):
        if start_idx == len(digits):
            return 1

        if start_idx in memo:
            return memo[start_idx]

        if digits[start_idx] == '0':
            return 0

        cur_sum = 0
        if start_idx < len(digits) - 1 and (digits[start_idx] == '1' or digits[start_idx] == '2' and int(digits[start_idx + 1]) <= 6):
            cur_sum += dfs(start_idx + 2)
        cur_sum += dfs(start_idx + 1)

        memo[start_idx] = cur_sum
        return cur_sum

    memo = {}
    return dfs(0)
