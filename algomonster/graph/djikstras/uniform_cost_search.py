from heapq import heappop, heappush


# Djikstra's but terminate search when destination node is reached
def shortest_path(graph, a, b):
    queue = [(0, a)]
    distances = [float('inf')] * len(graph)
    distances[a] = 0

    while queue:
        distance, node = heappop(queue)
        if node == b:
            return distance
        if distance > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            neighbor_distance = distances[node] + weight
            if distances[neighbor] <= neighbor_distance:
                continue
            heappush(queue, (neighbor_distance, neighbor))
            distances[neighbor] = neighbor_distance

    return distances[b] if distances[b] != float('inf') else -1
