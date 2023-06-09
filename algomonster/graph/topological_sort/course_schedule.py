from collections import deque


def is_valid_course_schedule(n, prerequisites):
    graph = {}
    indegrees = {}
    for node in range(n):
        graph[node] = []
        indegrees[node] = 0

    for first, second in prerequisites:
        indegrees[second] += 1
        graph[first].append(second)

    queue = deque()
    for node in range(n):
        if indegrees[node] == 0:
            queue.append(node)

    nodes = 0
    while queue:
        node = queue.popleft()
        nodes += 1

        for neighbor in graph[node]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return nodes == n
