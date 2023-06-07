from collections import deque


def task_scheduling(tasks, requirements):
    graph = {task: [] for task in tasks}
    indegrees = {task: 0 for task in tasks}
    for a, b in requirements:
        graph[a].append(b)
        indegrees[b] += 1

    queue = deque()
    for task in indegrees:
        if indegrees[task] == 0:
            queue.append(task)

    order = []
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for neighbor in graph[cur]:
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return order
