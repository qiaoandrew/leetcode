from heapq import heappush, heappop


def find_kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heappush(min_heap, num)
        if len(min_heap) > k:
            heappop(min_heap)

    return heappop(min_heap)
