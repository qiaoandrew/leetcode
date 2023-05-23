class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1, root2):
    if not root1:
        return root2

    if not root2:
        return root1

    return TreeNode(root1.val + root2.val, merge_trees(root1.left, root2.left),
                    merge_trees(root1.right, root2.right))
