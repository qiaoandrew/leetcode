def product_except_self(nums):
    res = [1] * len(nums)

    left_running_sum = 1
    right_running_sum = 1

    for i in range(len(nums)):
        res[i] *= left_running_sum
        res[len(nums) - 1 - i] *= right_running_sum

        left_running_sum *= nums[i]
        right_running_sum *= nums[len(nums) - 1 - i]

    return res


print(product_except_self([1, 2, 3, 4]))
