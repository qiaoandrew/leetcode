def move_zeros(nums):
    next_idx = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[next_idx], nums[i] = nums[i], nums[next_idx]
            next_idx += 1
    return next_idx
