def subsets(nums):
    res = []

    cur = []

    def dfs(i):
        if i == len(nums):
            res.append(cur[::])
            return

        cur.append(nums[i])

        dfs(i + 1)

        cur.pop()

        dfs(i + 1)

    dfs(0)

    return res


print(subsets([0]))
