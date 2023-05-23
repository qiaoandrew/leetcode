# Ordering such that every node appears before all nodes it points to
# Not unique
# Only for graphs without cycles
# Implemented using Kahn's Algorithm, similar to BFS

# Steps
# 1. Initialize hashmap to store in-degrees
# 2. Go through nodes, count in-degree of each node
# 3. Push nodes with 0 in-dgree into queue
# 4. Pop each node from queue, subtract 1 from in-degree of each of neighbors
# 5. If node's in-=degree drops to 0, push into queue
# 6. Repeat until queue is empty, if any nodes left, there is a cycle

from collections import deque


def topological_sort(graph):
    res = []
    queue = deque()

    indegrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1

    for node in indegrees:
        if indegrees[node] == 0:
            queue.append(node)

    while len(queue) > 0:
        node = queue.popleft()
        res.append(node)

        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return res if len(graph) == len(res) else None