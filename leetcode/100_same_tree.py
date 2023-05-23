def is_same_tree(p, q):

    def check_same(node1, node2):
        if not node1 and not node2:
            return True
        elif (not node1 or not node2) or (node1.val != node2.val):
            return False
        else:
            return check_same(node1.left, node2.left) and check_same(
                node1.right, node2.right)

    return check_same(p, q)
