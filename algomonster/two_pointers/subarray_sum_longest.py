def subarray_sum_longest(nums, target):
    longest = 0
    cur = 0
    left = 0
    for right in range(len(nums)):
        cur += nums[right]
        while cur > target:
            cur -= nums[left]
            left += 1
        longest = max(longest, right - left + 1)
    return longest
