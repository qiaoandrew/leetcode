from collections import defaultdict


def subarrays_div_by_k(nums, k):
    remainder_freq = defaultdict(int)
    remainder_freq[0] = 1

    res = 0
    prefix_sum = 0

    for num in nums:
        prefix_sum += num
        remainder = prefix_sum % k
        res += remainder_freq[remainder]
        remainder_freq[remainder] += 1

    return res
