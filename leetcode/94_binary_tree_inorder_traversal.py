def inorder_traversal(root):
    if not root:
        return []

    inorder = []

    def dfs(node):
        if node.left:
            dfs(node.left)

        inorder.append(node.val)

        if node.right:
            dfs(node.right)

    dfs(root)

    return inorder
