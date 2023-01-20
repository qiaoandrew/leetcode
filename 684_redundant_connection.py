from collections import defaultdict


def find_redundant_connection(edges):
    graph = defaultdict(set)

    def dfs(source, target, visited):
        if source in visited:
            return False
        elif source == target:
            return True

        visited.add(source)

        return any(
            dfs(neighbor, target, visited) for neighbor in graph[source])

    for node1, node2 in edges:
        visited = set()

        if node1 in graph and node2 in graph and dfs(node1, node2, visited):
            return [node1, node2]

        graph[node1].add(node2)
        graph[node2].add(node1)
