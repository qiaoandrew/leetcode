def kth_smallest(root, k):
    stack = []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()

        k -= 1

        if k == 0:
            return cur.val

        cur = cur.right

    return -1