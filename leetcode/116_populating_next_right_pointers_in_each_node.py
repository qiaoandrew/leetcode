from collections import deque


class Node:

    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    if not root:
        return None

    queue = deque([root])

    while queue:
        row_length = len(queue)

        for i in range(len(queue)):
            node = queue.popleft()

            if i == row_length - 1:
                node.next = None
            else:
                node.next = queue[0]

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    return root