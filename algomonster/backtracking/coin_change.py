def coin_change(coins, amount):
    def dfs(cur_amount, num_coins):
        if cur_amount == amount:
            return num_coins

        min_coins = float('inf')
        for coin in coins:
            if cur_amount + coin <= amount:
                min_coins = min(min_coins, dfs(
                    cur_amount + coin, num_coins + 1))

        return min_coins

    res = dfs(0, 0)
    return res if res != float('inf') else -1
