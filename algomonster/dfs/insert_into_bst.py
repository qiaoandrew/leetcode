class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst, val):
    if not bst:
        return Node(val)
    
    def dfs(node):
        if node.val == val:
            return
        elif node.val < val:
            if node.right:
                dfs(node.right)
            else:
                node.right = Node(val)
        else:
            if node.left:
                dfs(node.left)
            else:
                node.left = Node(val)
    
    dfs(bst)
    return bst