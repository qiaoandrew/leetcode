def good_nodes(root):

    def get_num_good(node, max_so_far):
        if not node:
            return 0

        if node.val >= max_so_far:
            return 1 + get_num_good(node.left, node.val) + get_num_good(
                node.right, node.val)
        else:
            return get_num_good(node.left, max_so_far) + get_num_good(
                node.right, max_so_far)

    return get_num_good(root, float('-inf'))
