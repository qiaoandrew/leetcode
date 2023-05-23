from collections import deque
from heapq import heappush, heappop


# Shortest-Path Faster Algorihtm (SPFA)
# Use distance hash table to keep track of shortest distance from source node to current node
# Source node starts at 0, others start at infinity
# Visit neighbor nodes of current node, check if possible to update distances to shorter value using current node as intermediate point
# If possible, update distance and add neighbor node to queue
# Repeat until queue is empty
# Time: O(n * m) where n is number of nodes and m is number of edges
def shortest_path(graph, root, target):
    queue = deque([root])
    distance = [float('inf')] * len(graph)
    distance[root] = 0

    while queue:
        node = queue.popleft()

        for neighbor, weight in graph[node]:
            if distance[neighbor] <= distance[node] + weight:
                continue

            queue.append(neighbor)
            distance[neighbor] = distance[node] + weight

    return distance[target] if distance != float('inf') else -1


# Djikstra's Algorithm
# More efficient that SPFA, uses fact that graph is weighted
# Priority queue to store unprocessed nodes and use distacne from source as priority
# Pop node with shortest disstance and process it
def djikstra(graph, root, target):
    min_heap = [(0, root)]
    distances = [float('inf')] * len(graph)
    distances[root] = 0

    while min_heap:
        distance, node = heappop(min_heap)

        if node == target:
            return distance

        if distance > distances[node]:
            continue

        for neighbor, neighbor_weight in graph[node]:
            neighbor_distance = distances[node] + neighbor_weight

            if distances[neighbor] <= neighbor_distance:
                continue

            heappush(min_heap, (neighbor_distance, neighbor))
            distances[neighbor] = neighbor_distance

    return -1