def find_duplicate(nums):
    for num in nums:
        val = abs(num)

        if nums[val - 1] < 0:
            return abs(val)

        nums[val - 1] *= -1

    return -1


print(find_duplicate([3, 1, 3, 4, 2]))
