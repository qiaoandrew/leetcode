from heapq import heappush, heappop


def merge_k_sorted_lists(lists):
    min_heap = []
    for list_idx in range(len(lists)):
        # value, list index, value index in its list
        heappush(min_heap, (lists[list_idx][0], list_idx, 0))

    res = []
    while min_heap:
        val, list_idx, val_idx = heappop(min_heap)
        res.append(val)
        if val_idx + 1 < len(lists[list_idx]):
            heappush(min_heap, (lists[list_idx]
                     [val_idx + 1], list_idx, val_idx + 1))

    return res
