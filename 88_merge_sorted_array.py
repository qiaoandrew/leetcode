def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    res_pointer = len(nums1) - 1

    while p1 >= 0 or p2 >= 0:
        if p1 == -1 or (p2 >= 0 and nums1[p1] < nums2[p2]):
            nums1[res_pointer] = nums2[p2]
            p2 -= 1
        else:
            nums1[res_pointer] = nums1[p1]
            p1 -= 1

        res_pointer -= 1

    return nums1


print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
