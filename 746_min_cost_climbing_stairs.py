def min_cost_climbing_stairs(cost):
    if len(cost) == 1:
        return 0

    min_cost = [0] * (len(cost) + 1)

    for i in range(2, len(cost) + 1):
        min_cost[i] = min(min_cost[i - 1] + cost[i - 1],
                          min_cost[i - 2] + cost[i - 2])

    return min_cost[-1]


print(min_cost_climbing_stairs([10, 15, 20]))
print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
