from collections import deque

def max_sliding_window(nums, k):
    res = []
    monotonic_indices = deque()

    for i in range(len(nums)):
        while monotonic_indices and nums[monotonic_indices[-1]] < nums[i]:
            monotonic_indices.pop()

        monotonic_indices.append(i)

        if monotonic_indices[0] == i - k:
            monotonic_indices.popleft()

        if i >= k - 1:
            res.append(nums[monotonic_indices[0]])
    
    return res