# Choose smallest weighted edge and continuously grow tree by one edge until n - 1 edges

def minimum_spanning_tree(n, edges):
    edges.sort(key=lambda x: x.weight)
    dsu = UnionFind()
    ans = 0
    count = 0
    for edge in edges:
        if dsu.find(edge.a) != dsu.find(edge.b):
            dsu.union(edge.a, edge.b)
            ans += edge.weight
            count += 1
            if count == n - 1:
                break
    return ans
