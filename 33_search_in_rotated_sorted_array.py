def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] > nums[-1]:
            if target > nums[mid] or target <= nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[mid] < target <= nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
