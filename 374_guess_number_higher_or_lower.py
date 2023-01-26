def guess_number(n):
    left, right = 1, n

    while left <= right:
        mid = (left + right) // 2
        res = guess(mid)

        if res == 0:
            return mid
        elif res == 1:
            left = mid + 1
        else:
            right = mid - 1

    return -1
