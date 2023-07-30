from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "None"
        else:
            return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(nodes):
            cur = nodes.pop(0)
            if cur == "None":
                return None
            else:
                node = TreeNode(int(cur))
                node.left = dfs(nodes)
                node.right = dfs(nodes)
                return node

        nodes = data.split(",")
        return dfs(nodes)