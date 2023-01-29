from collections import heapq
import math


def k_closest(points, k):
    max_heap = []

    for x, y in points:
        distance = math.sqrt(x**2 + y**2)
        heapq.heappush(max_heap, (-distance, (x, y)))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [val[1] for val in max_heap]