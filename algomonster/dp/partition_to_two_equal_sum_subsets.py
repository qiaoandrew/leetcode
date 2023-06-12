
def can_partition_brute_force(nums):
    def target_exists(cur_idx, cur_sum, target):
        if cur_sum == target:
            return True
        if cur_idx == len(nums) or cur_sum > target:
            return False
        return target_exists(cur_idx + 1, cur_sum + nums[cur_idx], target) or target_exists(cur_idx + 1, cur_sum, target)

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    target = total_sum // 2
    return target_exists(0, 0, target)


def can_parition_top_down(nums):
    def target_exists(cur_idx, cur_sum, target):
        if cur_sum == target:
            return True

        if cur_idx == len(nums) or cur_sum > target:
            return False

        if dp[cur_idx][cur_sum] == 0:
            exists = target_exists(
                cur_idx + 1, cur_sum + nums[cur_idx], target) or target_exists(cur_idx + 1, cur_sum, target)
            if exists:
                dp[cur_idx][cur_sum] = 1
                return True
            else:
                dp[cur_idx][cur_sum] = 2
                return False
        elif dp[cur_idx][cur_sum] == 1:
            return True
        else:
            return False

    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    target = total_sum // 2

    # 0: not visited
    # 1: visited, True
    # 2: visited, False
    dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    return target_exists(0, 0, target)


def can_partition_bottom_up(nums):
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False
    target = total_sum // 2
    dp = [[False for _ in range(target + 1)] for _ in range(len(nums) + 1)]
    dp[0][0] = True

    for i in range(1, len(nums) + 1):
        for cur_sum in range(target + 1):
            if cur_sum >= nums[i - 1]:
                dp[i][cur_sum] = dp[i - 1][cur_sum] or dp[i -
                                                          1][cur_sum - nums[i - 1]]
            else:
                dp[i][cur_sum] = dp[i - 1][cur_sum]

    return dp[len(nums)][target]


def can_parition_bottom_up_optimized(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [[False for _ in range(target + 1)] for _ in range(2)]
    dp[0][0] = True

    for i in range(1, len(nums) + 1):
        for cur_sum in range(target + 1):
            if cur_sum >= nums[i - 1]:
                dp[1][cur_sum] = dp[0][cur_sum] or dp[0][cur_sum - nums[i - 1]]
            else:
                dp[1][cur_sum] = dp[0][cur_sum]
        for cur_sum in range(target + 1):
            dp[0][cur_sum] = dp[1][cur_sum]
            dp[1][cur_sum] = False

    return dp[0][target]
