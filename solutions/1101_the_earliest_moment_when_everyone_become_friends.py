class UnionFind:

    def __init__(self, size):
        self.roots = [node for node in range(size)]
        self.ranks = [1] * size

    def find(self, node):
        if self.roots[node] != node:
            self.roots[node] = self.find(self.roots[node])

        return self.roots[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.ranks[root1] == self.ranks[root2]:
            self.roots[root2] = root1
            self.ranks[root1] += 1
        elif self.ranks[root1] < self.ranks[root2]:
            self.roots[root1] = root2
        else:
            self.roots[root2] = root1

        return True


class Solution:

    def earliest_acq(self, logs, n):
        logs.sort(key=lambda log: log[0])

        union_find = UnionFind(n)

        groups = n

        for timestamp, friend1, friend2 in logs:
            if union_find.union(friend1, friend2):
                groups -= 1

            if groups == 1:
                return timestamp

        return -1