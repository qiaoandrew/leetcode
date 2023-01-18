def combination_sum_2(candidates, target):
    candidates.sort()

    res = []

    cur_combination = []

    def backtrack(i, cur_sum):
        if cur_sum == target:
            res.append(cur_combination[:])
            return

        if i == len(candidates) or cur_sum > target:
            return

        cur_combination.append(candidates[i])
        backtrack(i + 1, cur_sum + candidates[i])

        while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
            i += 1
        cur_combination.pop()
        backtrack(i + 1, cur_sum)

    backtrack(0, 0)

    return res