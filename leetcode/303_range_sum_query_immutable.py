class NumArray:

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [0] * len(nums)

        running_sum = 0

        for i in range(len(nums)):
            running_sum += nums[i]
            self.prefix_sum[i] = running_sum

    def sum_range(self, left, right):
        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[left]