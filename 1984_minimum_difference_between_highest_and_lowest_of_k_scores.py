def minimum_difference(nums, k):
    if k == 1:
        return 0

    nums.sort()

    res = float('inf')

    for i in range(len(nums) - k + 1):
        res = min(res, nums[i + k - 1] - nums[i])

    return res


print(minimum_difference([90], 1))
print(minimum_difference([9, 4, 1, 7], 2))
