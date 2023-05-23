from collections import defaultdict


def leads_to_destination(n, edges, source, destination):
    graph = defaultdict(set)
    # 1: node has been checked and is correct, -1: node is in current path and cycle has occurred
    visited = defaultdict(int)

    for [node1, node2] in edges:
        graph[node1].add(node2)

    def dfs(node):
        if visited[node] == 1:
            return True
        elif visited[node] == -1:
            return False
        elif len(graph[node]) == 0:
            return node == destination
        else:
            visited[node] = -1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 1

            return True

    return dfs(source)


print(leads_to_destination(3, [[0, 1], [0, 2]], 0, 2))
print(leads_to_destination(4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3))
print(leads_to_destination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3))
