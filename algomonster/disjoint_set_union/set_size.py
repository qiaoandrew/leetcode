class UnionFind:
    def __init__(self):
        self.roots = {}
        self.sizes = {}

    def find(self, x):
        root = self.roots.get(x, x)
        if root != x:
            root = self.find(root)
            self.roots[x] = root
        return root

    def union(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            self.sizes[x_root] = self.count(x_root) + self.count(y_root)
            self.roots[y_root] = self.find(x_root)

    def count(self, x):
        root = self.find(x)
        if root in self.sizes:
            return self.sizes[root]
        else:
            self.sizes[root] = 1
            return 1


class SetCounter:
    def __init__(self):
        self.dsu = UnionFind()

    def merge(self, x, y):
        self.dsu.union(x, y)

    def count(self, x):
        return self.dsu.count(x)
