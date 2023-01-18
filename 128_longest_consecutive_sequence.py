def longest_consecutive(nums):
    res = 0

    nums_set = set(nums)

    for num in nums:
        if num - 1 not in nums_set:
            length = 1

            while num + length in nums_set:
                length += 1

            res = max(res, length)

    return res


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
