import math
from heapq import heappush, heappop


def k_closest_points(points, k):
    max_heap = []
    for x, y in points:
        heappush(max_heap, (-math.sqrt(x ** 2 + y ** 2), (x, y)))
        if len(max_heap) > k:
            heappop(max_heap)
    return reversed([point for _, point in max_heap])
