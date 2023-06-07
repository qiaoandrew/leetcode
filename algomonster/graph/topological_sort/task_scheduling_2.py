from collections import defaultdict, deque


def task_scheduling_2(tasks, times, requirements):
    graph = defaultdict(list)
    task_times = {tasks[i]: times[i] for i in range(len(tasks))}
    indegrees = {task: 0 for task in tasks}

    for a, b in requirements:
        graph[a].append(b)
        indegrees[b] += 1

    total_task_times = {task: 0 for task in tasks}
    total_time = 0
    queue = deque()

    for task in tasks:
        if indegrees[task] == 0:
            total_task_times[task] = task_times[task]
            total_time = max(total_time, total_task_times[task])
            deque.append(task)

    while queue:
        cur = queue.popleft()

        for neighbor in graph[cur]:
            total_task_times[neighbor] = max(
                total_task_times[neighbor], total_task_times[cur] + task_times[neighbor])
            total_time = max(total_time, total_task_times[neighbor])
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return total_time
