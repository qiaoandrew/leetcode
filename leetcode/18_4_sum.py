def four_sum(nums, target):

    def two_sum(nums, target):
        res = []

        low, high = 0, len(nums) - 1

        while low < high:
            cur_sum = nums[low] + nums[high]

            if cur_sum < target or (low > 0 and nums[low] == nums[low - 1]):
                low += 1
            elif cur_sum > target or (high < len(nums) - 1
                                      and nums[high] == nums[high + 1]):
                high -= 1
            else:
                res.append([nums[low], nums[high]])
                low += 1
                high -= 1

        return res

    def k_sum(nums, target, k):
        if len(nums) == 0:
            return []
        elif k == 2:
            return two_sum(nums, target)

        res = []

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                sub_res = k_sum(nums[i + 1:], target - nums[i], k - 1)

                for subset in sub_res:
                    res.append(subset + [nums[i]])

        return res

    nums.sort()

    return k_sum(nums, target, 4)