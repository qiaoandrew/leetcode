from collections import heapq

# cheapest n - 1 connections that do not form a cycle


class UnionFind:

    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.ranks = [1] * size

    def find(self, x):
        if self.roots[x] == x:
            return x

        self.roots[x] = self.find(self.roots[x])

        return self.roots[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if self.ranks[root_x] > self.ranks[root_y]:
            self.roots[root_y] = root_x
        elif self.ranks[root_x] < self.ranks[root_y]:
            self.roots[root_x] = root_y
        else:
            self.roots[root_y] = root_x
            self.ranks[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Edge:

    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class KruscalSolution:

    def min_cost_connect_points(self, points):
        size = len(points)
        priority_queue = []
        union_find = UnionFind(size)

        for i in range(size - 1):
            x1, y1 = points[i]

            for j in range(i + 1, size):
                x2, y2 = points[j]

                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)

                priority_queue.append(edge)

        heapq.heapify(priority_queue)

        cost = 0
        paths_needed = size - 1

        while priority_queue and paths_needed > 0:
            edge = heapq.heappop(priority_queue)

            if not union_find.connected(edge.point1, edge.point2):
                cost += edge.cost
                paths_needed -= 1
                union_find.union(edge.point1, edge.point2)

        return cost


class PrimSolution:

    def min_cost_connect_points(self, points):
        size = len(points)
        priority_queue = []
        visited = set()

        min_cost = 0
        paths_needed = size - 1

        x1, y1 = points[0]

        for j in range(1, size):
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            edge = Edge(0, j, cost)
            priority_queue.append(edge)

        heapq.heapify(priority_queue)

        visited.add(0)

        while priority_queue and paths_needed > 0:
            edge = heapq.heappop(priority_queue)

            point2 = edge.point2
            cost = edge.cost

            if point2 not in visited:
                min_cost += cost
                visited.add(point2)

                for j in range(size):
                    if j not in visited:
                        distance = abs(points[point2][0] - points[j][0]) + \
                                   abs(points[point2][1] - points[j][1])
                        heapq.heappush(priority_queue,
                                       Edge(point2, j, distance))

                paths_needed -= 1

        return min_cost