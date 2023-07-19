def daily_temperatures(t):
    stack = []
    res = [0] * len(t)
    for i in range(len(t)):
        while stack and t[stack[-1]] < t[i]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res