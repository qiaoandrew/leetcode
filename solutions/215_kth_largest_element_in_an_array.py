from collections import heapq


def find_kth_largest(nums, k):
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]