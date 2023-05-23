from collections import defaultdict


def subarray_sum(nums, k):
    running_sum = 0

    prefix_sum_occurences = defaultdict(int)
    prefix_sum_occurences[0] = 1

    res = 0

    for i in range(len(nums)):
        running_sum += nums[i]
        res += prefix_sum_occurences[running_sum - k]

        prefix_sum_occurences[running_sum] += 1

    return res


print(subarray_sum([1, 2, 3], 3))
