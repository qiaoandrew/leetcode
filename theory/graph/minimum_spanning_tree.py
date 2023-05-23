from collections import heapq

# Spanning tree: Connected subgraph in undirected graph where all vertices are connected with minimum number of edges
# Minimum spanning tree: Spanning tree with minimum possible total edge weight in a weighted undirected graph
# Cut property: Edge with least weight belongs to all MSTs of graph

# Kruskal and Prim are algorithms that construct minimum spanning tree of weighted undirected graph

# Kruskal's algorithm
# 1. Sort all edges in ascending order by weight (priority queue)
# 2. Try every edge, as long as 2 nodes of that edge are not currently connected by a path, then add new edge to graph (disjoint set union)
# 3. Repeat 2 until n - 1 edges have been added
# Time: O(E * log E)
# Space: O(V)


class Kruskal:

    def min_cost_connect_points(self, points):
        # Sort all edges by cost in a priority queue
        size = len(points)
        priority_queue = []
        disjoint_set_union = DisjointSet(size)

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

        # Pop edge with least weight until n - 1 edges
        while priority_queue and paths_needed > 0:
            edge = heapq.heappop(priority_queue)

            if not disjoint_set_union.connected(edge.point1, edge.point2):
                cost += edge.cost
                paths_needed -= 1
                disjoint_set_union.union(edge.point1, edge.point2)

        return cost


# Prim's Algorithm:
# 1. Start at arbitrary node
# 2. Push all neighboring edges of node into priority queue
# 3. If node edge leads to has not been visited, add edge to tree and push neighbouring edges
# 4. Reepat until n - 1 edges selected
# Time: O(E * log V) for binary heap, O(E + V * log V) for Fibonacci heap
# Space: O(V)


class Prim:

    def min_cost_connect_points(self, points):
        size = len(points)
        priority_queue = []
        visited = set()

        min_cost = 0
        paths_needed = size - 1

        # Add all edges of first point into priority queue
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


class DisjointSet:

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

    def union_simple(self, x, y):
        self.roots[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Edge:

    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost
