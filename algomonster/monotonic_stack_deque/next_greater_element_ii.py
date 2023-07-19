def next_greater_elements(nums):
    next_greater = [-1] * len(nums)
    stack = []
    for i in range(len(nums) * 2):
        actual_i = i % len(nums)
        while stack and nums[stack[-1]] < nums[actual_i]:
            idx = stack.pop()
            next_greater[idx] = nums[actual_i]
        stack.append(actual_i)
    return next_greater
