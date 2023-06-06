from collections import deque
from string import ascii_letters

def word_ladder(begin, end, word_list):
    def get_neighbors(word):
        neighbors = []
        for i in range(len(word)):
            for c in ascii_letters:
                neighbor = word[:i] + c + word[i + 1:]
                if neighbor in word_list and neighbor not in visited:
                    neighbors.append(neighbor)
                    visited.add(neighbor)
        return neighbors
    
    word_list_set = set(word_list)
    queue = deque([begin])
    visited = set([begin])
    steps = 0
    
    while queue:
        for _ in range(len(queue)):
            cur_word = queue.popleft()
            if cur_word == end:
                return steps
            for word in get_neighbors(cur_word):
                queue.append(word)
        steps += 1
    
    return -1