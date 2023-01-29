def next_greater_element(nums1, nums2):
    next_greater = {}

    stack = []

    for i in range(len(nums2)):
        while stack and nums2[stack[-1]] < nums2[i]:
            j = stack.pop()

            next_greater[nums2[j]] = nums2[i]

        stack.append(i)

    ans = [-1] * len(nums1)

    for i in range(len(nums1)):
        if nums1[i] in next_greater:
            ans[i] = next_greater[nums1[i]]

    return ans


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_element([2, 4], [1, 2, 3, 4]))
