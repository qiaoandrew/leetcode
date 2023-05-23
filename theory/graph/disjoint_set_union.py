# Use Disjoint Set / Union Find to quickly check if two vertices are connected

# Parent node: Direct parent node of vertex
# Root node: Node without parent node, can be viewed as parent of itself


# Constructor: O(N)
# Find: O(1)
# Union: O(N)
# Connected: O(1)
class QuickFind:

    def __init__(self, size):
        self.roots = [i for i in range(size)]

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            for i in range(len(self.root)):
                if self.roots[i] == root_y:
                    self.roots[i] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Constructor: O(N)
# Find: O(N)
# Union: O(N)
# Connected: O(N)
class QuickUnion:

    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Optimizes union function for quick find
# Constructor: O(N)
# Find: O(logN)
# Union: O(logN)
# Connected: O(logN)
class UnionByRank:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Optimizes find function for quick union
# Constructor: O(N)
# Find: O(logN)
# Union: O(logN)
# Connected: O(logN)
class PathCompression:

    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Most optimized version
# Constructor: O(N)
# Find: O(a(N))
# Union: O(a(N))
# Connected: O(a(N))
# a is Inverse Ackermann function, assume its constant
# O(a(N)) is O(1) on average
class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)