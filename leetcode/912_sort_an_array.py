def sort_array(nums):

    def merge(nums, left, mid, right):
        left_half, right_half = nums[left:mid + 1], nums[mid + 1:right + 1]
        nums_idx, left_idx, right_idx = left, 0, 0

        while left_idx < len(left_half) or right_idx < len(right_half):
            if right_idx == len(
                    right_half) or left_idx[left_idx] <= right_half[right_idx]:
                nums[nums_idx] = left_half[left_idx]
                left_idx += 1
            else:
                nums[nums_idx] = right_half[right_idx]
                right_idx += 1

            nums_idx += 1

        return nums

    def merge_sort(nums, left, right):
        if left == right:
            return nums

        mid = (left + right) // 2

        merge_sort(nums, left, mid)
        merge_sort(nums, mid + 1, right)

        merge(nums, left, mid, right)

        return nums

    return merge_sort(nums, 0, len(nums) - 1)
