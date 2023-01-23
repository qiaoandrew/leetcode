def coin_change(coins, amount):
    dp = {i: float('inf') for i in range(amount + 1)}
    dp[0] = 0

    for coin in coins:
        for cur_amount in range(amount + 1):
            if coin <= cur_amount:
                dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - coin] + 1)

    return dp[amount]


print(coin_change([1, 2, 5], 11))
