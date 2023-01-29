def sorted_squares(nums):
    left, right = 0, len(nums) - 1

    res = []

    while left <= right:
        left_sqr = nums[left]**2
        right_sqr = nums[right]**2

        if left_sqr > right_sqr:
            res.append(left_sqr)
            left += 1
        else:
            res.append(right_sqr)
            right -= 1

    return reversed(res)