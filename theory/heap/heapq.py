import heapq

heap = []
heapq.heappush(heap, (5, 'write code'))
heapq.heappush(heap, (7, 'release product'))
heapq.heappush(heap, (1, 'write spec'))
heapq.heappush(heap, (3, 'create tests'))
print(heapq.heappop(heap))
print(heap[0])
