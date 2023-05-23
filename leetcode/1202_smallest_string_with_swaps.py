from collections import defaultdict


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

        if root_x != root_y:
            if self.ranks[root_x] > self.ranks[root_y]:
                self.roots[root_y] = root_x
            elif self.ranks[root_x] < self.ranks[root_y]:
                self.roots[root_x] = root_y
            else:
                self.roots[root_y] = root_x
                self.ranks[root_x] += 1


class UnionFindSolution:

    # union indices that can be interchanged
    # hash root to possible indices and characters that can fill that position
    # loop through indices and characters from hash map
    # sort indices and chars, loop through them and set index to character
    def smallest_string_with_swaps(self, s, pairs):
        union_find = UnionFind(len(s))

        for node1, node2 in pairs:
            union_find.union(node1, node2)

        root_to_indices_and_chars = defaultdict(lambda: ([], []))

        for index, char in enumerate(s):
            root = union_find.find(index)
            root_to_indices_and_chars[root][0].append(index)
            root_to_indices_and_chars[root][1].append(char)

        res = [''] * len(s)

        for indices, chars in root_to_indices_and_chars.values():
            indices.sort()
            chars.sort()

            for index, char in zip(indices, chars):
                res[index] = char

        return ''.join(res)


solution = UnionFindSolution()
print(solution.smallest_string_with_swaps('dcab', [[0, 3], [1, 2]]))
print(solution.smallest_string_with_swaps('dcab', [[0, 3], [1, 2], [0, 2]]))
print(solution.smallest_string_with_swaps('cba', [[0, 1], [1, 2]]))
