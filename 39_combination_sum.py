def combination_sum(candidates, target):
    res = []

    cur_combination = []

    def backtrack(i, cur_sum):
        if cur_sum == target:
            res.append(cur_combination[::])
            return

        if i == len(candidates) or cur_sum > target:
            return

        cur_combination.append(candidates[i])
        backtrack(i, cur_sum + candidates[i])

        cur_combination.pop()
        backtrack(i + 1, cur_sum)

    backtrack(0, 0)

    return res


print(combination_sum([2, 3, 6, 7], 7))
