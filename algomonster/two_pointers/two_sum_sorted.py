def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        cur = arr[left] + arr[right]
        if cur > target:
            right -= 1
        elif cur < target:
            left += 1
        else:
            return [left, right]
    return [-1, -1]
