from collections import defaultdict

def delete_and_earn(nums):
    points_per_num = defaultdict(int)
    max_num = nums[0]
    for num in nums:
        points_per_num[num] += num
        max_num = max(max_num, num)
    
    dp = [0] * (max_num + 1)
    dp[1] = points_per_num[1]
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 2] + points_per_num[i], dp[i - 1])
    
    return dp[-1]