def max_area(height):
    res = 0

    left, right = 0, len(height) - 1

    while left < right:
        res = max(res, min(height[left], height[right]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return res


print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
