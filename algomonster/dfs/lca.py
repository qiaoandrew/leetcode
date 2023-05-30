def lca(root, node1, node2):
    if not root:
        return None
    
    if root.val == node1.val or root.val == node2.val:
        return root
    
    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    if left and right:
        return root
    elif left:
        return left
    elif right:
        return right
    
    return None