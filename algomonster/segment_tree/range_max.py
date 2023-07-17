class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (4 * len(arr))
        for i in range(len(arr)):
            self.update(1, 0, len(arr) - 1, i, arr[i])
    
    def update(self, cur, cur_left, cur_right, idx, val):
        if idx == cur_left == cur_right:
            self.tree[cur] = val
        else:
            cur_mid = (cur_left + cur_right) // 2
            if idx <= cur_mid:
                self.update(cur * 2, cur_left, cur_mid, idx, val)
            else:
                self.update(cur * 2 + 1, cur_mid + 1, cur_right, idx, val)
            self.tree[cur] = max(self.tree[cur * 2], self.tree[cur * 2 + 1])
    
    def query(self, cur, cur_left, cur_right, query_left, query_right):
        if cur_left > query_right or cur_right < query_left:
            return 0
        elif query_left <= cur_left and cur_right <= query_right:
            return self.tree[cur]
        cur_mid = (cur_left + cur_right) // 2
        return max(self.query(cur * 2, cur_left, cur_mid, query_left, query_right), self.query(cur * 2 + 1, cur_mid + 1, cur_right, query_left, query_right))

def range_max(arr, operations):
    tree = SegmentTree(arr)
    ans = []
    for (operation, left, right) in operations:
        if operation == 1:
            ans.append(tree.query(1, 0, len(arr) - 1, left, right))
        else:
            tree.update(1, 0, len(arr) - 1, left, right)
    return ans