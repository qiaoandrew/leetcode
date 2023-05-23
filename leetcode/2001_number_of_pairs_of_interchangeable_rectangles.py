from collections import defaultdict


def interchangeableRectangles(rectangles):
    res = 0

    width_to_height_ratio_count = defaultdict(int)

    for width, height in rectangles:
        res += width_to_height_ratio_count[width / height]
        width_to_height_ratio_count[width / height] += 1

    return res
