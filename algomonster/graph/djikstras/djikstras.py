from heapq import heappush, heappop


# Use priority queue to store nodes by distance from root node
def shortest_path(graph, a, b):
    queue = []
    distances = []
    for node in range(len(graph)):
        heappush(queue, (0 if node == a else float('inf'), node))
        distances.append(0 if node == a else float('inf'))

    while queue:
        _, node = heappop(queue)
        for neighbor, weight in graph[node]:
            neighbor_distance = distances[node] + weight
            if distances[neighbor] <= neighbor_distance:
                continue
            distances[neighbor] = neighbor_distance
            heappush(queue, (neighbor_distance, neighbor))

    return distances[b] if distances[b] != float('inf') else -1
