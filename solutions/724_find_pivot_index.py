def pivot_index(nums):
    running_sum = 0
    total_sum = sum(nums)

    for i in range(len(nums)):
        if running_sum * 2 == total_sum - nums[i]:
            return i

        running_sum += nums[i]

    return -1
