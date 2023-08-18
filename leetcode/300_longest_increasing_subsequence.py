def length_of_lis(nums):
    dp = [1] * len(nums)
    max_len = 1
    for i in range(1, len(dp)):
        for prev in range(i):
            if nums[i] > nums[prev]:
                dp[i] = max(dp[i], dp[prev] + 1)
                max_len = max(max_len, dp[i])
    return max_len