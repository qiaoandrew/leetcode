def brute_force(weights):
    res = set()

    def dfs(i, cur_sum):
        if i == len(weights):
            res.add(cur_sum)
            return

        cur_sum += weights[i]
        dfs(i + 1, cur_sum)

        cur_sum -= weights[i]
        dfs(i + 1, cur_sum)

    dfs(0, 0)

    return list(res)


def top_down_dp(weights):
    n = len(weights)
    total_sum = sum(weights)

    res = set()

    memo = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]

    def dfs(weight_idx, cur_sum):
        if memo[weight_idx][cur_sum]:
            return

        if weight_idx == len(weights):
            res.add(cur_sum)
            return

        cur_sum += weights[weight_idx]
        dfs(weight_idx + 1, cur_sum)

        cur_sum -= weights[weight_idx]
        dfs(weight_idx + 1, cur_sum)

        memo[weight_idx][cur_sum] = True

    dfs(0, 0)

    return list(res)


def bottom_up_dp(weights):
    n = len(weights)
    total_sum = sum(weights)

    dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]
    dp[0][0] = True

    for first_i_elements in range(1, n + 1):
        for weight in range(0, total_sum + 1):
            dp[first_i_elements][weight] = dp[first_i_elements][weight] or dp[
                first_i_elements - 1][weight]

            if weight - weights[first_i_elements - 1] >= 0:
                dp[first_i_elements][weight] = dp[first_i_elements][
                    weight] or dp[first_i_elements - 1][weight -
                                                        weights[i - 1]]

    res = []

    for weight in range(0, total_sum + 1):
        if dp[n][weight]:
            res.append(weight)

    return res


print(top_down_dp([1, 3, 3, 5]))