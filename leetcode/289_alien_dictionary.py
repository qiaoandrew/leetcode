from collections import defaultdict, deque

def alien_order(words):
    characters = set()
    for word in words:
        for char in word:
            characters.add(char)
    
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    for i in range(len(words) - 1):
        word_1, word_2 = words[i], words[i + 1]
        for i in range(min(len(word_1), len(word_2))):
            if word_1[i] != word_2[i]:
                if word_2[i] not in graph[word_1[i]]:
                    in_degree[word_2[i]] += 1
                    graph[word_1[i]].add(word_2[i])
                break
        else:
            if len(word_1) > len(word_2):
                return ""
    
    queue = deque()
    for char in characters:
        if in_degree[char] == 0:
            queue.append(char)

    order = []
    while queue:
        char = queue.popleft()
        order.append(char)
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return "".join(order) if len(order) == len(characters) else ""

print(alien_order(["z", "x", "z"]))
print(alien_order(["wrt","wrf","er","ett","rftt"]))