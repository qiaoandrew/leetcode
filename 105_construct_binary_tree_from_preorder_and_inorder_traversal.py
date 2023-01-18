class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    root_idx = inorder.index(preorder[0])

    root.left = build_tree(preorder[1:root_idx + 1], inorder[:root_idx])
    root.right = build_tree(preorder[root_idx + 1:], inorder[root_idx + 1:])

    return root
