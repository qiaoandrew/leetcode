from heapq import heappush, heappop


def minimum_spanning_tree(n, edges):
    graph = {node: [] for node in range(n)}
    for edge in edges:
        graph[edge.a].append((edge.weight, edge.b))
    queue = []
    for weight, neighbor in graph[0]:
        heappush(queue, (weight, neighbor))
    res = 0
    visited = set([0])
    while queue:
        weight, node = heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        res += weight
        for neighbor_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heappush(queue, (neighbor_weight + weight, neighbor))
        if len(visited) == n - 1:
            return res
    return res
