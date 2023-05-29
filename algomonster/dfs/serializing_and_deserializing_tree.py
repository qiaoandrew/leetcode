class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    serialization = []

    def dfs(node):
        if not node:
            serialization.append('x')
            return
        
        serialization.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ','.join(serialization)

def deserialize(s):
    nodes = s.split(',')
    cur_idx = 0

    def dfs():
       nonlocal cur_idx

       if cur_idx >= len(nodes):
           return None
       elif nodes[cur_idx] == 'x':
           cur_idx += 1
           return None
       else:
           node = Node(int(nodes[cur_idx]))
           cur_idx += 1
           node.left = dfs()
           node.right = dfs()
           return node
        
    return dfs()

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.right = Node(6)

print(serialize(deserialize('1,2,3,x,x,x,6,x,x')))