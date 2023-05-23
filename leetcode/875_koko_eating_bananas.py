import math


def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    res = max(piles)

    while left <= right:
        mid = (left + right) // 2

        time_required = 0

        for pile in piles:
            time_required += math.ceil(pile / mid)

        if time_required <= h:
            res = min(res, mid)
            right = mid - 1
        else:
            left = mid + 1

    return res


print(min_eating_speed([3, 6, 7, 11], 8))
