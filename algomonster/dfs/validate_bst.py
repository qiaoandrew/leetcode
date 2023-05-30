def valid_bst(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True

        if not min_val <= node.val < max_val:
            return False
        
        return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)

    return dfs(root, float('-inf'), float('inf'))