from heapq import heappush, heappop


def reorganize_string(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    max_heap = []
    for char in count:
        heappush(max_heap, (-count[char], char))
    res = []
    while max_heap:
        char_count, char = heappop(max_heap)
        if len(res) > 0 and res[-1] == char:
            if len(max_heap) == 0:
                return ''
            char_2_count, char_2 = heappop(max_heap)
            res.append(char_2)
            if char_2_count < -1:
                heappush(max_heap, (char_2_count + 1, char_2))
            heappush(max_heap, (char_count, char))
        else:
            res.append(char)
            if char_count < -1:
                heappush(max_heap, (char_count + 1, char))
    return ''.join(res)


print(reorganize_string('aab'))
