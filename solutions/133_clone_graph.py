class Node:

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    node_to_clone = {None: None}

    def dfs(node):
        if node in node_to_clone:
            return node_to_clone[node]

        cloned_node = Node(node.val)

        node_to_clone[node] = cloned_node

        for neighbor in node.neighbors:
            cloned_node.neighbors.append(dfs(neighbor))

        return cloned_node

    return dfs(node)