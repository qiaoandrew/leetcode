from heapq import heappush, heappop


def kth_smallest(matrix, k):
    min_heap = []

    for row_idx in range(len(matrix)):
        # value, row_idx, value_idx
        heappush(min_heap, (matrix[row_idx][0], row_idx, 0))

    for i in range(k):
        if not min_heap:
            return None

        value, row_idx, value_idx = heappop(min_heap)
        if i == k - 1:
            return value

        if value_idx + 1 < len(matrix[row_idx]):
            heappush(min_heap, (matrix[row_idx]
                     [value_idx + 1], row_idx, value_idx + 1))
