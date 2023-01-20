# create adjacency list
# visited set
# dfs traverse adjacency list starting from 0
# dfs gets prev node parameter
# if node is in visited return False
def valid_tree(n, edges):
    if not n:
        return True

    adj = {i: [] for i in range(n)}
    for node1, node2 in edges:
        adj[node1].append(node2)
        adj[node2].append(node1)

    visited = set()

    def dfs(node, prev):
        if node in visited:
            return False

        visited.add(node)

        for neighbor in adj[node]:
            if neighbor == prev:
                continue
            if not dfs(neighbor, node):
                return False

        return True

    return dfs(0, -1) and n == len(visited)