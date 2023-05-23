def max_profit(prices):
    res = 0

    for price_idx in range(1, len(prices)):
        if prices[price_idx] > prices[price_idx - 1]:
            res += prices[price_idx] - prices[price_idx - 1]

    return res
