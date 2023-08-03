def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for cur_amount in range(len(dp)):
        for coin in coins:
            if cur_amount >= coin:
                dp[cur_amount] = min(dp[cur_amount], dp[cur_amount - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1


print(coin_change([1, 2, 5], 11))
