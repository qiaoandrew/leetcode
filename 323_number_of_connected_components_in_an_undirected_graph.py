def count_components(n, edges):
    adjacency_list = {i: [] for i in range(n)}

    for node1, node2 in edges:
        adjacency_list[node1].append(node2)
        adjacency_list[node2].append(node1)

    res = 0
    visited = set()

    def dfs(node):
        visited.add(node)

        for neighbor in adjacency_list[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in range(n):
        if node not in visited:
            res += 1
            dfs(node)

    return res