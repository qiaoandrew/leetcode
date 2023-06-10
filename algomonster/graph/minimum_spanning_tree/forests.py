class UnionFind:
    def __init__(self, num):
        self.roots = {i: 0 for i in range(num)}

    def find(self, x):
        root = self.roots.get(x, x)
        if root != x:
            self.roots[x] = self.find(root)
        return self.roots[x]

    def union(self, x, y):
        self.roots[self.find(x)] = self.find(y)

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


def mst_forest(trees, pairs):
    pairs.sort(key=lambda pair: pair[2])
    uf = UnionFind(trees)
    ans = 0
    count = 0
    for pair in pairs:
        if not uf.is_connected(pair[0], pair[1]):
            uf.union(pair[0], pair[1])
            ans += pair[2]
            count += 1
            if count == trees - 1:
                break
    return ans
