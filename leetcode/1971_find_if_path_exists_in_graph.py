from collections import defaultdict, deque


class DFSSolution:

    def valid_path(self, n, edges, source, destination):
        adj_list = defaultdict(list)

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()

        def dfs(source, destination):
            if source == destination:
                return True

            visited.add(source)

            for neighbor in adj_list[source]:
                if neighbor not in visited and dfs(neighbor, destination):
                    return True

            return False

        return dfs(source, destination)


class BFSSolution:

    def valid_path(self, n, edges, source, destination):
        adj_list = defaultdict(list)

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        queue = deque([source])
        visited = set([source])

        while queue:
            node = queue.popleft()

            if node == destination:
                return True

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False


class DisjointSet:

    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size

    def find(self, x):
        if self.roots[x] == x:
            return x

        self.roots[x] = self.find(self.roots[x])

        return self.roots[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.ranks[root_x] > self.ranks[root_y]:
                self.roots[root_y] = root_x
            elif self.ranks[root_x] < self.ranks[root_y]:
                self.roots[root_x] = root_y
            else:
                self.roots[root_y] = root_x
                self.ranks[root_x] += 1


class DisjointSetSolution:

    def valid_path(self, n, edges, source, destination):
        disjoint_set = DisjointSet(n)

        for node1, node2 in edges:
            disjoint_set.union(node1, node2)

        return disjoint_set.find(source) == disjoint_set.find(destination)