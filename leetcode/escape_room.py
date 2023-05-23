from collections import deque

m = int(input())
n = int(input())

grid = [[0 for _ in range(n)] for _ in range(m)]

for row in range(m):
    line = input()

    nums = line.split(' ')

    for col in range(n):
        grid[row][col] = int(nums[col])

queue = deque([(1, 1)])
visited = set()

while queue:
    row, col = queue.popleft()

    if (row, col) in visited or row > m or col > n:
        continue

    if row == m and col == n:
        print('yes')
        exit(0)

    val = grid[row - 1][col - 1]
    visited.add((row, col))

    for divisor in range(1, val + 1):
        if val % divisor == 0:
            queue.append((divisor, val // divisor))
            queue.append((val // divisor, divisor))

print('no')