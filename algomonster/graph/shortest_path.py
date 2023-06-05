from collections import deque


def shortest_path(graph, a, b):
    queue = deque([a])
    visited = set([a])
    length = 0

    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()

            if node == b:
                return length

            for neighbor in graph[node]:
                queue.append(neighbor)
                visited.add(neighbor)
        length += 1

    return -1
