

def knapsack_weight_only_top_down(weights):
    ans = set()

    def dfs(idx, cur_sum):
        if memo[idx][cur_sum]:
            return

        if idx == len(weights):
            ans.add(cur_sum)
            return

        dfs(idx + 1, cur_sum + weights[idx])
        dfs(idx + 1, cur_sum)
        memo[idx][cur_sum] = True

    total_sum = sum(weights)
    memo = [[False for _ in range(total_sum + 1)]
            for _ in range(len(weights) + 1)]
    dfs(0, 0)

    return list(ans)


def knapsack_weight_only_bottom_up(weights):
    n = len(weights)
    total_sum = sum(weights)

    dp = [[False for _ in range(total_sum + 1)]
          for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n + 1):
        for weight in range(total_sum + 1):
            dp[i][weight] = dp[i][weight] or dp[i - 1][weight]

            if weight >= weights[i - 1]:
                dp[i][weight] = dp[i][weight] or dp[i - 1][weight - weights[i - 1]]

    ans = []
    for weight in range(total_sum + 1):
        if dp[n][weight]:
            ans.append(weight)

    return ans


def knapsack_weight_only_bottom_up_optimized(weights):
    n = len(weights)
    total_sum = sum(weights)

    dp = [[False for _ in range(total_sum + 1)] for _ in range(2)]
    dp[0][0] = True

    for i in range(n + 1):
        for weight in range(total_sum + 1):
            dp[1][weight] = dp[1][weight] or dp[0][weight]

            if weight >= weights[i - 1]:
                dp[1][weight] = dp[1][weight] or dp[0][weight - weights[i - 1]]

        for weight in range(total_sum + 1):
            dp[0][weight] = dp[1][weight]

    ans = []
    for weight in range(total_sum + 1):
        if dp[0][weight]:
            ans.append(weight)

    return ans
