def subsets_with_dup(nums):
    nums.sort()

    res = []

    cur_subset = []

    def backtrack(i):
        if i == len(nums):
            res.append(cur_subset[:])
            return

        cur_subset.append(nums[i])
        backtrack(i + 1)

        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1

        cur_subset.pop()
        backtrack(i + 1)

    backtrack(0)

    return res


print(subsets_with_dup([1, 2, 2]))
