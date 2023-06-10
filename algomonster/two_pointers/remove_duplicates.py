def remove_duplcates(arr):
    next_idx = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[next_idx] = arr[i]
            next_idx += 1
    return next_idx
