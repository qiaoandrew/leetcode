from collections import defaultdict, deque


def sequence_reconstruction(original, seqs):
    graph = defaultdict(list)
    indegrees = {node: 0 for node in original}

    for seq in seqs:
        for i in range(len(seq) - 1):
            graph[seq[i]].append(seq[i + 1])
            indegrees[seq[i + 1]] += 1

    queue = deque()
    for num in indegrees:
        if indegrees[num] == 0:
            queue.append(num)

    sequence = []
    while queue:
        if len(queue) > 1:
            return False

        cur = queue.popleft()
        sequence.append(cur)

        for neighbor in graph[cur]:
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    return original == sequence
