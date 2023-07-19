from collections import deque

def sliding_window_maximum(nums, k):
    maximums = []
    monotonic_queue = deque()
    left = 0
    for right in range(len(nums)):
        while len(monotonic_queue) > 0 and nums[right] >= monotonic_queue[-1][1]:
            monotonic_queue.pop()
        monotonic_queue.append((right, nums[right]))
        if right - left + 1 == k:
            maximums.append(monotonic_queue[0][1])
            if len(monotonic_queue) > 0 and monotonic_queue[0][0] == left:
                monotonic_queue.popleft()
            left += 1
    return maximums

print(sliding_window_maximum([1, 3, 2, 5, 8, 7], 3))