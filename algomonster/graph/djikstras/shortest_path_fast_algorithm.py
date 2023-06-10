from collections import deque


# Not efficient as doesn't take advantage of fact that graph is weighted
def shortest_path(graph, a, b):
    queue = deque([a])
    distance = [float('inf')] * len(graph)
    distance[a] = 0

    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if distance[neighbor] <= distance[node] + weight:
                continue
            queue.append(neighbor)
            distance[neighbor] = distance[node] + weight

    return distance[b] if distance[b] != float('inf') else -1
