def is_valid_bst(root):

    def get_valid(node, min_val, max_val):
        if not node:
            return True

        if min_val < node.val < max_val:
            return get_valid(node.left, min_val, node.val) and get_valid(
                node.right, node.val, max_val)
        else:
            return False

    return get_valid(root, float('-inf'), float('inf'))