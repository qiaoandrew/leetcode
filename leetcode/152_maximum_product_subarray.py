def maxProduct(nums):
    res = nums[0]
    cur_min, cur_max = 1, 1
    for num in nums:
        cur_min, cur_max = min(cur_min * num, cur_max * num, num), max(cur_min * num, cur_max * num, num)
        res = max(res, cur_max)
    return res