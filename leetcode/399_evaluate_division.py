from collections import defaultdict


# 1. Build nested defaultdict out of list of input equations {node1 : {node2: node1 / node2}}
# 2. DFS each query while keeping an acumulative product
#    If no connection or either node doesn't exist, -1.0
#    If same node, 1.0
class DFSSolution:

    def calc_equation(self, equations, values, queries):
        graph = defaultdict(defaultdict)

        def dfs(source, destination, product, visited):
            visited.add(source)

            if source == destination:
                return product

            for neighbor in graph[source]:
                if neighbor in visited:
                    continue

                answer = dfs(neighbor, destination,
                             product * graph[source][neighbor], visited)

                if answer != -1.0:
                    return answer

            return -1.0

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        answers = []

        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                answers.append(-1.0)
            elif dividend == divisor:
                answers.append(1.0)
            else:
                visited = set()
                answers.append(dfs(dividend, divisor, 1, visited))

        return answers


# 1. For each input equation, union(dividend, divisor, quotient)
# 2. Evaluate each query, if either doesn't appear: -1.0, not in same group: -1.0, same group: division between their weights
class UnionFindSolution:

    def calc_equation(equations, values, queries):
        group_id_weight = {}

        def find(node_id):
            if node_id not in group_id_weight:
                group_id_weight[node_id] = (node_id, 1)

            group_id, node_weight = group_id_weight[node_id]

            if group_id != node_id:
                new_group_id, group_weight = find(group_id)
                group_id_weight[node_id] = (new_group_id,
                                            node_weight * group_weight)

            return group_id_weight[node_id]

        def union(dividend, divisor, value):
            pass


solution = DFSSolution()

print(
    solution.calc_equation(
        [["a", "b"], ["b", "c"]], [2.0, 3.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print(
    solution.calc_equation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
print(
    solution.calc_equation([["a", "b"]], [0.5],
                           [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
