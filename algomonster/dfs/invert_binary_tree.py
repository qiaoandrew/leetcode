def invert_binary_tree(tree):
    if not tree:
        return None
    
    tree.left, tree.right = tree.right, tree.left
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)

    return tree