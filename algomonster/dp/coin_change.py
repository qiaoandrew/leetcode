def coin_change_brute_force(coins, amount):
    def dfs(path, cur_sum):
        if cur_sum == amount:
            return len(path)
        elif cur_sum > amount:
            return -1

        min_coins = float('inf')
        for coin in coins:
            path.append(coin)
            res = dfs(path, cur_sum + coin)
            if res != -1:
                min_coins = min(min_coins, res)
            path.pop()

        return min_coins if min_coins != float('inf') else -1

    return dfs([], 0)


def coin_change_top_down(coins, amount):
    def dfs(path, cur_sum):
        if cur_sum == amount:
            return len(path)
        elif cur_sum > amount:
            return -1

        sorted_hashable_path = tuple(sorted(path))
        if sorted_hashable_path in memo:
            return memo[sorted_hashable_path]

        min_coins = float('inf')
        for coin in coins:
            path.append(coin)
            res = dfs(path, cur_sum + coin)
            if res != -1:
                min_coins = min(min_coins, res)
            path.pop()

        memo[sorted_hashable_path] = min_coins if min_coins != float(
            'inf') else -1
        return memo[sorted_hashable_path]

    memo = {}
    return dfs([], 0)


def coin_change_bottom_up(coins, amount):
    dp = [float('inf') for _ in range(amount + 1)]
    dp[0] = 0

    for cur_amount in range(1, amount + 1):
        for coin in coins:
            if cur_amount >= coin:
                dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - coin] + 1)

    return dp[-1] if dp[-1] != float('inf') else -1
