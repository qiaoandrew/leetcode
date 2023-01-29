class UnionFind:

    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size
        self.count = size

    def find(self, x):
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])

        return self.roots[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.ranks[root_x] == self.ranks[root_y]:
                self.roots[root_y] = root_x
                self.ranks[root_x] += 1
            elif self.ranks[root_x] < self.ranks[root_y]:
                self.roots[root_x] = root_y
            else:
                self.roots[root_y] = root_x

            self.count -= 1

    def get_count(self):
        return self.count