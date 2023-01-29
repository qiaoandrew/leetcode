class UnionFind:

    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size
        self.count = size

    def find(self, x):
        if self.roots[x] == x:
            return x

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


class UnionFindSolution:

    def findCircleNum(self, is_connected):
        n = len(is_connected)
        unionFind = UnionFind(n)

        for node1 in range(n - 1):
            for node2 in range(node1 + 1, n):
                if is_connected[node1][node2] == 1:
                    unionFind.union(node1, node2)

        return unionFind.get_count()


class DFSSolution:

    def find_circle_num(self, is_connected):
        n = len(is_connected)
        res = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in range(n):
                if is_connected[node][
                        neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        return res