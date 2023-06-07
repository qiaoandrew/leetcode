# 1. Hashmap to store in-degrees
# 2. Queue to store nodes with 0 in-degree
# 3. Pop nodes, subtract 1 from in-degree of each neighbor
# 4. If neighbor's in-degree is 0, push into queue
# 5. Repeat until queue is empty

from collections import deque


def topological_sort(graph):
    sort = []
    queue = deque()

    indegrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1

    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    while queue:
        cur = queue.popleft()
        sort.append(cur)

        for neighbor in graph[cur]:
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return sort if len(graph) == len(sort) else []
