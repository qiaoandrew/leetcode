def lca_on_bst(bst, p, q):
    if bst.val > p and bst.val > q:
        return lca_on_bst(bst.left, p, q)
    elif bst.val < p and bst.val < q:
        return lca_on_bst(bst.right, p, q)
    else:
        return bst.val