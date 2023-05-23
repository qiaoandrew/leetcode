from collections import heapq, defaultdict


class Solution:

    def network_delay_time(self, times, n, k):
        edges = defaultdict(list)

        for source, target, weight in times:
            edges[source].append((target, weight))

        min_heap = [(0, k)]
        visited = set()
        delay_time = 0

        while min_heap:
            weight1, node1 = heapq.heappop(min_heap)

            if node1 in visited:
                continue

            delay_time = weight1
            visited.add(node1)

            for node2, weight2 in edges[node1]:
                if node2 not in visited:
                    heapq.heappush(min_heap, (weight1 + weight2, node2))

        return delay_time if len(visited) == n else -1
