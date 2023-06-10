def subarray_sum(arr, target):
    prefix_sums = {0: 0}
    cur_sum = 0

    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1

    return [-1, -1]
