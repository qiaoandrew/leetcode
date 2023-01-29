def rob(nums):
    if len(nums) == 1:
        return nums[0]

    rob1, rob2 = 0, 0

    for num in nums:
        new_rob = max(rob1 + num, rob2)

        rob1 = rob2
        rob2 = new_rob

    return new_rob


print(rob([1, 2, 3, 1]))
