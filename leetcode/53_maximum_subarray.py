def max_subarray(nums):
    cur_sum = 0
    max_sum = float('-inf')
    for num in nums:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    return max_sum