import heapq


class MedianOfStream:

    def __init__(self):
        self.upper_half_min_heap = []
        self.lower_half_max_heap = []

    def add_number(self, num):
        if len(self.upper_half_min_heap
               ) == 0 or num > self.upper_half_min_heap[0]:
            heapq.heappush(self.upper_half_min_heap, num)

            if len(self.upper_half_min_heap) > len(
                    self.lower_half_max_heap) + 1:
                num = heapq.heappop(self.upper_half_min_heap)
                heapq.heappush(self.lower_half_max_heap, -num)
        else:
            heapq.heappush(self.lower_half_max_heap, -num)

            if len(self.lower_half_max_heap) > len(self.upper_half_min_heap):
                num = -heapq.heappop(self.lower_half_max_heap)
                heapq.heappush(self.upper_half_min_heap, num)

    def get_median(self):
        if len(self.upper_half_min_heap) > len(self.lower_half_max_heap):
            return self.upper_half_min_heap[0]
        else:
            return (-self.lower_half_max_heap[0] +
                    self.upper_half_min_heap[0]) / 2
