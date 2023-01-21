# adjacency list
# visited set
# dfs each node starting at 0, if node is already in visited return false
# pass a parent param to avoid false positives
def valid_tree(n, edges):
    if n == 0:
        return True

    adjacency_list = {i: [] for i in range(n)}

    for node1, node2 in edges:
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)

    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False

        visited.add(node)

        for neighbor in adjacency_list[node]:
            if neighbor != parent:
                if not dfs(neighbor, node):
                    return False

        return True

    return dfs(0, -1) and len(visited) == n
