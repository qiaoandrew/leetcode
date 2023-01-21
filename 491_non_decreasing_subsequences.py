def find_subsequences(nums):
    res = set()
    cur = []

    def backtrack(i):
        if i == len(nums):
            if len(cur) >= 2:
                res.add(tuple(cur))
            return

        if len(cur) == 0 or cur[-1] <= nums[i]:
            cur.append(nums[i])
            backtrack(i + 1)
            cur.pop()

        backtrack(i + 1)

    backtrack(0)

    return list(res)