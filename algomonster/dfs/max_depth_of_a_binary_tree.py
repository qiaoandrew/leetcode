def tree_max_depth(root):
    def dfs(root):
        if not root:
            return 0
        
        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) - 1 if root else 0