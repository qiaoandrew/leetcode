class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []

        self.val = val
        self.chidlren = children

def ternary_tree_paths(root):
    def dfs(node, cur_path):
        if not node.children:
            all_paths.append('->'.join(cur_path))
            return
        
        for child in node.children:
            cur_path.append(str(child.val))
            dfs(child, cur_path)
            cur_path.pop()

    all_paths = []
    if root: dfs(root, [str(root.val)])
    return all_paths