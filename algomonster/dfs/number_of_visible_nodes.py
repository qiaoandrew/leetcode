def visible_tree_node(root):
    def dfs(node, greatest_so_far):
        if not node:
            return 0
        elif node.val >= greatest_so_far:
            return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
        else:
            return dfs(node.left, greatest_so_far) + dfs(node.right, greatest_so_far)
    return dfs(root, -float('inf'))