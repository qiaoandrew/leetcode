def find_largest_subset(nums):
    nums.sort()
    dp = [1 for _ in range(len(nums))]
    longest = 1
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
                longest = max(longest, dp[i])
    return longest
