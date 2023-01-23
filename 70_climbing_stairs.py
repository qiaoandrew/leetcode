def climb_stairs(n):
    if n == 1:
        return 1

    res = [1] * (n + 1)

    for i in range(2, n + 1):
        res[i] = res[i - 1] + res[i - 2]

    return res[-1]


print(climb_stairs(2))
print(climb_stairs(3))