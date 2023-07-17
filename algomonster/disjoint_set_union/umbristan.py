class UnionFind:
    def __init__(self, n):
        self.roots = {i: i for i in range(1, n + 1)}
        self.count = n

    def find(self, x):
        root = self.roots[x]
        if root != x:
            root = self.find(root)
            self.roots[x] = root
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.roots[root_x] = self.roots[root_y]
            self.count -= 1

    def count(self):
        return self.count


class UnionByRank:
    def __init__(self, n):
        self.roots = {i: i for i in range(1, n + 1)}
        self.ranks = {i: 0 for i in range(1, n + 1)}
        self.count = n

    def find(self, x):
        root = self.roots[x]
        if root != x:
            root = self.find(root)
            self.roots[x] = root
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.ranks[self.find(x)] < self.ranks[self.find(y)]:
                self.roots[self.find(x)] = self.find(y)
            else:
                self.roots[self.find(y)] = self.find(x)
                if self.ranks[self.find(x)] == self.ranks[self.find(y)]:
                    self.ranks[self.find(x)] += 1
            self.count -= 1

    def count(self):
        return self.count


def umbristan(n, breaks):
    union_find = UnionByRank(n)
    res = [0] * len(breaks)
    for break_idx in range(len(res) - 1, -1, -1):
        res[break_idx] = union_find.count
        node1, node2 = breaks[break_idx]
        union_find.union(node1, node2)
    return res


print(umbristan(4, [[1, 2], [2, 3], [3, 4], [1, 4], [2, 4]]))
