def mincost_tickets(days, costs):
    dp = [0] * (days[-1] + 1)

    i = 0
    for day in range(1, len(dp)):
        if days[i] != day:
            dp[day] = dp[day - 1]
        else:
            dp[day] = min(
                dp[day - 1] + costs[0],
                dp[max(0, day - 7)] + costs[1],
                dp[max(0, day - 30)] + costs[2],
            )
            i += 1
    
    return dp[-1]