def has_path_sum(root, target_sum):
    if not root:
        return False

    stack = [(root, root.val)]

    while stack:
        cur_node, cur_sum = stack.pop()

        if cur_node.left is None and cur_node.right is None and cur_sum == target_sum:
            return True

        if cur_node.left:
            stack.append((cur_node.left, cur_sum + cur_node.left.val))

        if cur_node.right:
            stack.append((cur_node.right, cur_sum + cur_node.right.val))

    return False