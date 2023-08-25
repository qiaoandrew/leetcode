from collections import Counter
import heapq

def reorganize_string(s):
    frequencies = Counter(s)
    max_heap = [(-freq, char) for char, freq in frequencies.items()]
    heapq.heapify(max_heap)

    prev_freq, prev_char = 0, ''
    result = []
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        prev_freq, prev_char = freq + 1, char
    
    if len(result) != len(s):
        return ''
    
    return ''.join(result)