from collections import deque


class DFSSolution:

    def all_paths_source_target(self, graph):
        all_paths = []

        def dfs(node, path):
            if node == len(graph) - 1:
                all_paths.append(path[:])
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor, path)
                path.pop()

        dfs(0, [0])

        return all_paths


class BFSSolution:

    def all_paths_source_target(self, graph):
        all_paths = []

        queue = deque([[0, []]])

        while queue:
            node, path = queue.popleft()

            if node == len(graph) - 1:
                all_paths.append(path[:])
                continue

            for neighbor in graph[node]:
                path.append(neighbor)
                queue.append([neighbor, path[:]])
                path.pop()

        return all_paths