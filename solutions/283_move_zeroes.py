def move_zeroes(nums):
    next_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[next_non_zero] = nums[next_non_zero], nums[i]
            next_non_zero += 1

    return nums


print(move_zeroes([0, 1, 0, 3, 12]))
