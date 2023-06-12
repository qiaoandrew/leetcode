class UnionFind:
    def __init__(self):
        self.roots = {}

    def find(self, x):
        root = self.roots.get(x, x)
        if root != x:
            root = self.find(root)
            self.roots[x] = root
        return root

    def union(self, x, y):
        self.roots[self.find(x)] = self.find(y)


class UnionByRank:
    def __init__(self):
        self.roots = {}
        self.ranks = {}

    def find(self, x):
        root = self.roots.get(x, x)
        if root != x:
            root = self.find(root)
            self.roots[x] = root
        return root

    def union(self, x, y):
        if self.find(x) not in self.ranks:
            self.ranks[self.find(x)] = 0
        if self.find(y) not in self.ranks:
            self.ranks[self.find(y)] = 0

        if self.ranks[self.find(x)] < self.ranks[self.find(y)]:
            self.roots[self.find(x)] = self.find(y)
        else:
            self.roots[self.find(y)] = self.find(x)
            if self.ranks[self.find(x)] == self.ranks[self.find(y)]:
                self.ranks[self.find(x)] += 1


class SameSet:
    def __init__(self):
        self.union_find = UnionFind()

    def merge(self, x, y):
        self.union_find.union(x, y)

    def is_same(self, x, y):
        return self.union_find.find(x) == self.union_find.find(y)
