from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view(root):
    if not root:
        return []
    right_side = []
    queue = deque([root])
    while queue:
        right_side.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return right_side
