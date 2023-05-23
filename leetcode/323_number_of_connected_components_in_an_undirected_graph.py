from collections import defaultdict


class DFSSolution:
    # make adjacency list
    # dfs each node not in visited set, increment counter
    def count_components(self, n, edges):
        adjacency_list = defaultdict(list)

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
                dfs(node)
                res += 1

        return res


class UnionFind:

    def __init__(self, size):
        self.roots = [node for node in range(size)]
        self.ranks = [1] * size

    def find(self, node):
        if self.roots[node] == node:
            return node

        self.roots[node] = self.find(self.roots[node])
        return self.roots[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.ranks[root1] == self.ranks[root2]:
                self.roots[root2] = root1
                self.ranks[root1] += 1
            elif self.ranks[root1] < self.ranks[root2]:
                self.roots[root1] = root2
            else:
                self.roots[root2] = root1


class UnionFindSolution:

    def count_components(self, n, edges):
        union_find = UnionFind(n)

        for node1, node2 in edges:
            union_find.union(node1, node2)

        roots_set = set()

        for root in union_find.roots:
            roots_set.add(union_find.find(root))

        return len(roots_set)