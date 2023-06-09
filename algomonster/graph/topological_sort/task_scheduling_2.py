from collections import defaultdict, deque


def task_scheduling_2(tasks, times, requirements):
    task_times = {}
    for task, time in zip(tasks, times):
        task_times[task] = time

    graph = {task: [] for task in tasks}
    indegrees = {task: 0 for task in tasks}
    for before, after in requirements:
        graph[before].append(after)
        indegrees[after] += 1

    ans = 0
    total_task_times = {task: 0 for task in tasks}
    queue = deque()
    for task in tasks:
        if indegrees[task] == 0:
            ans = max(ans, task_times[task])
            total_task_times[task] = task_times[task]
            queue.append(task)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            total_task_times[neighbor] = max(
                total_task_times[neighbor], total_task_times[node] + task_times[neighbor])
            ans = max(ans, total_task_times[neighbor])
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return ans
