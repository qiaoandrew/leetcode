from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zig_zag_traversal(root):
    if not root:
        return []

    traversal = []
    queue = deque([root])
    reverse = False

    while queue:
        cur_level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            cur_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if reverse:
            traversal.append(cur_level[::-1])
        else:
            traversal.append(cur_level)
        reverse = not reverse

    return traversal
