def sort_colors(nums):
    next_zero = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[next_zero], nums[i] = nums[i], nums[next_zero]
            next_zero += 1

    next_one = next_zero

    for i in range(next_one, len(nums)):
        if nums[i] == 1:
            nums[next_one], nums[i] = nums[i], nums[next_one]
            next_one += 1

    return nums


print(sort_colors([2, 0, 2, 1, 1, 0]))
print(sort_colors([2, 0, 1]))
