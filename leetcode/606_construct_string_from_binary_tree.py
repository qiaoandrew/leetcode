def tree_2_str(root):
    string = []

    def dfs(node):
        string.append(str(node.val))

        if not node.left and not node.right:
            return

        string.append('(')

        if node.left:
            dfs(node.left)

        string.append(')')

        if node.right is not None:
            string.append('(')

            dfs(node.right)

            string.append(')')

    dfs(root)

    return ''.join(string)