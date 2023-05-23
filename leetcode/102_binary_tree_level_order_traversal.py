from collections import deque


def level_order(root):
    if not root:
        return []

    res = []

    queue = deque([root])

    while queue:
        row = []

        for _ in range(len(queue)):
            node = queue.popleft()

            row.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        res.append(row)

    return res
