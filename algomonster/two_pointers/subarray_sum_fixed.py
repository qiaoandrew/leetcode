def subarray_sum_fixed(nums, k):
    largest = float('-inf')
    cur = 0
    left = 0
    for right in range(len(nums)):
        cur += nums[right]
        if right - left + 1 > k:
            cur -= nums[left]
            left += 1
        largest = max(largest, cur)
    return largest
