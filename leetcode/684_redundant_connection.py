from collections import defaultdict


# loop through edges, populate adjacency set for neighbors
# if there is already a path between the two nodes, current edge is redundant, return it
# use dfs to check for a path
def find_redundant_connection(edges):
    graph = defaultdict(set)

    def dfs(source, target, visited):
        if source in visited:
            return False

        if source == target:
            return True

        visited.add(source)

        return any(
            dfs(neighbor, target, visited) for neighbor in graph[source])

    for node1, node2 in edges:
        if node1 in graph and node2 in graph:
            visited = set()

            if dfs(node1, node2, visited):
                return [node1, node2]

        graph[node1].add(node2)
        graph[node2].add(node1)
