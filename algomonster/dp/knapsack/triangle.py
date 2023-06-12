def minimum_total_brute_force(triangle):
    def get_min(val_idx, row_idx, cur_sum):
        if row_idx == len(triangle):
            return cur_sum
        return min(get_min(val_idx, row_idx + 1, cur_sum + triangle[row_idx][val_idx]), get_min(val_idx + 1, row_idx + 1, cur_sum + triangle[row_idx][val_idx]))

    return get_min(0, 0, 0)


def minimum_total_top_down(triangle):
    def get_min(val_idx, row_idx, cur_sum):
        if (val_idx, row_idx, cur_sum) in memo:
            return memo[(val_idx, row_idx, cur_sum)]
        if row_idx == len(triangle):
            return cur_sum
        res = min(get_min(val_idx, row_idx + 1, cur_sum + triangle[row_idx][val_idx]), get_min(
            val_idx + 1, row_idx + 1, cur_sum + triangle[row_idx][val_idx]))
        memo[(val_idx, row_idx, cur_sum)] = res
        return res

    memo = {}
    return get_min(0, 0, 0)


def minimum_total_bottom_up(triangle):
    n = len(triangle)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for col_idx in range(n):
        dp[-1][col_idx] = triangle[-1][col_idx]
    for row_idx in range(n - 2, -1, -1):
        for col_idx in range(row_idx + 1):
            dp[row_idx][col_idx] = min(
                dp[row_idx + 1][col_idx], dp[row_idx + 1][col_idx + 1]) + triangle[row_idx][col_idx]
    return dp[0][0]


def minimimum_total_bottom_up_optimized(triangle):
    e


print(minimimum_total_bottom_up_optimized([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]))
