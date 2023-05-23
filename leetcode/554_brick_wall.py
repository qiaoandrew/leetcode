def least_bricks(wall):
    edges = {0: 0}

    for row in wall:
        total_width = 0

        for width in row[:-1]:
            total_width += width
            edges[total_width] = edges.get(total_width, 0) + 1

    return len(wall) - max(edges.values())


print(
    least_bricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2],
                  [1, 3, 1, 1]]))
print(least_bricks([[1], [1], [1]]))
