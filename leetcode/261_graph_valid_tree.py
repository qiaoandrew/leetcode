from collections import defaultdict


class DFSSolution:
    # adjacency list
    # visited set
    # dfs each node starting at 0, if node is already in visited return false
    # pass a parent param to avoid false positives
    def valid_tree(self, n, edges):
        adj_list = defaultdict(list)

        for node1, node2 in edges:
            adj_list[node1].append(node2)
            adj_list[node2].append(node1)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor != parent and not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n


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

        if root1 == root2:
            return False
        else:
            if self.ranks[root1] == self.ranks[root2]:
                self.roots[root2] = root1
                self.ranks[root1] += 1
            elif self.ranks[root1] < self.ranks[root2]:
                self.roots[root1] = root2
            else:
                self.roots[root2] = root1

            return True


class UnionFindSolution:

    def valid_tree(self, n, edges):
        if len(edges) != n - 1:
            return False

        union_find = UnionFind(n)

        for node1, node2 in edges:
            if not union_find.union(node1, node2):
                return False

        return True


ufTest = UnionFindSolution()
print(ufTest.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(ufTest.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
