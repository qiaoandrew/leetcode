def find_min_rotated(arr):
    left, right = 0, len(arr) - 1
    feasible_boundary = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= arr[-1]:
            feasible_boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return feasible_boundary