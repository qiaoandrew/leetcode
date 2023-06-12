def coin_game_brute_force(coins, amount):
    def dfs(start_idx, cur_sum):
        if cur_sum == amount:
            return 1
        elif cur_sum > amount:
            return 0

        res = 0
        for coin_idx in range(start_idx, len(coins)):
            res += dfs(coin_idx, cur_sum + coins[coin_idx])
        return res

    return dfs(0, 0)


def coin_game_top_down(coins, amount):
    def dfs(start_idx, cur_sum):
        if cur_sum == amount:
            return 1
        elif cur_sum > amount:
            return 0
        elif (start_idx, cur_sum) in memo:
            return memo[(start_idx, cur_sum)]

        res = 0
        for coin_idx in range(start_idx, len(coins)):
            res += dfs(coin_idx, cur_sum + coins[coin_idx])
        memo[(start_idx, cur_sum)] = res
        return res

    memo = {}
    return dfs(0, 0)


def coin_game_bottom_up(coins, amount):
    n = len(coins)
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for cur_sum in range(amount + 1):
            dp[i][cur_sum] = dp[i - 1][cur_sum]
            if cur_sum >= coins[i - 1]:
                dp[i][cur_sum] += dp[i][cur_sum - coins[i - 1]]

    return dp[n][amount]


def coin_game_bottom_up_optimized(coins, amount):
    n = len(coins)
    dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for cur_sum in range(amount + 1):
            dp[1][cur_sum] = dp[0][cur_sum]
            if cur_sum >= coins[i - 1]:
                dp[1][cur_sum] += dp[1][cur_sum - coins[i - 1]]
        for cur_sum in range(amount + 1):
            dp[0][cur_sum] = dp[1][cur_sum]

    return dp[0][amount]


print(coin_game_brute_force([1, 2, 5], 5))
print(coin_game_brute_force([2], 3))
