def lowest_common_ancestor(root, p, q):
    smaller = p.val if p.val < q.val else q.val
    bigger = q.val if p.val < q.val else p.val

    def get_lca(node):
        if smaller <= node.val <= bigger:
            return node
        elif node.val < smaller:
            return get_lca(node.right)
        else:
            return get_lca(node.left)

    return get_lca(root)
