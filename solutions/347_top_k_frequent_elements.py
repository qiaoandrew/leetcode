from collections import defaultdict
import heapq


def top_k_frequent_heap(nums, k):
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    min_heap = []

    for num, count in counts.items():
        min_heap.append((count, num))

    heapq.heapify(min_heap)

    while len(min_heap) > k:
        heapq.heappop(min_heap)

    return [pair[1] for pair in min_heap]


def top_k_frequent_array(nums, k):
    counts = defaultdict(int)

    for num in nums:
        counts[num] += 1

    frequencies = [[] for _ in range(len(nums) + 1)]

    for num, count in counts.items():
        frequencies[count].append(num)

    res = []

    for frequency in range(len(frequencies) - 1, -1, -1):
        while len(frequencies[frequency]) > 0:
            if len(res) == k:
                break

            res.append(frequencies[frequency].pop())

    return res


print(top_k_frequent_array([1], 1))
