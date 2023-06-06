from collections import deque

next_num = {
    '0': '1',
    '1': '2',
    '2': '3',
    '3': '4',
    '4': '5',
    '5': '6',
    '6': '7',
    '7': '8',
    '8': '9',
    '9': '0',
}

prev_num = {
    '0': '9',
    '1': '0',
    '2': '1',
    '3': '2',
    '4': '3',
    '5': '4',
    '6': '5',
    '7': '6',
    '8': '7',
    '9': '8'
}
    

def num_steps(target_combo, trapped_combos):
    trapped_combos_set = set(trapped_combos)
    visited = set(['0000'])
    queue = deque(['0000'])
    steps = 0

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur == target_combo:
                return steps
            for i in range(4):
                new_1 = cur[:i] + next_num[cur[i]] + cur[i + 1:]
                if new_1 not in visited and new_1 not in trapped_combos_set:
                    queue.append(new_1)
                    visited.add(new_1)
                new_2 = cur[:i] + prev_num[cur[i]] + cur[i + 1:]
                if new_2 not in visited and new_2 not in trapped_combos_set:
                    queue.append(new_2)
                    visited.add(new_2)
        steps += 1

    return -1
