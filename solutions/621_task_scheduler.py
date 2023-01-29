from collections import defaultdict, heapq, deque


# do tasks with higher frequency first
# hash map to map task to frequency
# add all frequencies to max heap
# use queue to track cooldown for tasks
def least_interval(tasks, n):
    counts = defaultdict(int)

    for task in tasks:
        counts[task] += 1

    max_heap = []

    for count in counts.values():
        heapq.heappush(max_heap, -count)

    task_queue = deque()

    time = 0

    while max_heap or task_queue:
        time += 1

        if max_heap:
            count = -heapq.heappop(max_heap) - 1

            if count > 0:
                task_queue.append((time + n, count))

        if task_queue and task_queue[0][0] == time:
            heapq.heappush(max_heap, -task_queue.popleft()[1])

    return time
