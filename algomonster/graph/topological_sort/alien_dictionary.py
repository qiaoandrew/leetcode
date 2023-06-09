from heapq import heappop, heappush\



def alien_order(words):
    graph = {}
    for word in words:
        for char in word:
            graph[char] = set()
    indegrees = {char: 0 for char in graph}

    for word_idx in range(len(words) - 1):
        first, second = words[word_idx], words[word_idx + 1]

        letter_idx = 0
        while letter_idx < len(first) and letter_idx < len(second):
            if first[letter_idx] != second[letter_idx]:
                if second[letter_idx] not in graph[first[letter_idx]]:
                    graph[first[letter_idx]].add(second[letter_idx])
                    indegrees[second[letter_idx]] += 1
                break
            letter_idx += 1

    min_heap = []
    for char in indegrees:
        if indegrees[char] == 0:
            heappush(min_heap, char)

    ans = []
    while min_heap:
        cur_letter = heappop(min_heap)
        ans.append(cur_letter)
        for neighbor in graph[cur_letter]:
            indegrees[neighbor] -= 1

            if indegrees[neighbor] == 0:
                heappush(min_heap, neighbor)

    for indegree in indegrees.values():
        if indegree != 0:
            return ''

    return ''.join(ans)
