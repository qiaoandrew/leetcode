def find_disappeared_numbers(nums):
    for i in range(len(nums)):
        idx = abs(nums[i]) - 1

        if nums[idx] > 0:
            nums[idx] *= -1

    res = []

    for i in range(len(nums)):
        if nums[i] > 0:
            res.append(i + 1)

    return res


print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disappeared_numbers([1, 1]))
