def peak_of_mountain_array(arr):
    left, right = 0, len(arr) - 1
    feasible_boundary = -1

    while left <= right:
        mid = (left + right) // 2
        if mid == len(arr) - 1 or arr[mid] > arr[mid + 1]:
            feasible_boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return feasible_boundary