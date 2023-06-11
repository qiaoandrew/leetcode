from heapq import heappush, heappop


class MedianOfDataStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_number(self, num):
        if not self.min_heap or num > self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)
        self._balance()

    def get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]

    def _balance(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            heappush(self.max_heap, -heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap):
            heappush(self.min_heap, -heappop(self.max_heap))
