def subarray_sum_shortest(nums, target):
    shortest = float('inf')
    cur = 0
    left = 0
    for right in range(len(nums)):
        cur += nums[right]
        while cur > target:
            cur -= nums[left]
            left += 1
            shortest = min(shortest, right - left + 1)
    return shortest
