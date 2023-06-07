from heapq import heappop, heappush


def alien_order(words):
    graph = {}
    for word in words:
        for char in word:
            graph[char] = []

    for word_idx in range(len(words) - 1):
        prev, cur = words[word_idx], words[word_idx + 1]

        letter_idx = 0
        while letter_idx < len(prev) and letter_idx < len(cur):
            if (prev[letter_idx] != cur[letter_idx]):
                if not cur[letter_idx] in graph[prev[letter_idx]]:
                    graph[prev[letter_idx]].append(cur[letter_idx])
                break
            letter_idx += 1

    indegrees = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegrees[neighbor] += 1

    order = []
    priority_queue = []

    for node in indegrees:
        if indegrees[node] == 0:
            heappush(priority_queue, node)

    while priority_queue:
        node = heappop(priority_queue)
        order.append(node)

        for neighbor in graph[node]:
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                heappush(priority_queue, neighbor)

    for indegree in indegrees.values():
        if indegree != 0:
            return ''

    return ''.join(order)


def alien_order_2(words):
    graph = {}
