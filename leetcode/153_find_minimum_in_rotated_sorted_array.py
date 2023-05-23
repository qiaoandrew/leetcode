def find_min(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


print(find_min([3, 4, 5, 1, 2]))
