from collections import deque


def right_side_view(root):
    if not root:
        return []

    res = []

    queue = deque([root])

    while queue:
        res.append(queue[-1].val)

        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)

    return res
