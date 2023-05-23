from collections import deque


class Node:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def level_order(self, root):
        if not root:
            return []

        levels = []

        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                level.append(node.val)

                for child in node.children:
                    queue.append(child)

            levels.append(level)

        return levels
