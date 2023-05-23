from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    queue = deque([root, root])

    while queue:
        node1 = queue.popleft()
        node2 = queue.popleft()

        if node1.val != node2.val:
            return False

        if node1.left and node2.right:
            queue.append(node1.left)
            queue.append(node2.right)
        elif node1.left or node2.right:
            return False

        if node1.right and node2.left:
            queue.append(node1.right)
            queue.append(node2.left)
        elif node1.right or node2.left:
            return False

    return True