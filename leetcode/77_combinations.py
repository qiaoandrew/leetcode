def combine(n, k):
    res = []
    def backtrack(i, cur_path):
        if len(cur_path) == k:
            res.append(cur_path[:])
            return
        elif i == n + 1:
            return
        cur_path.append(n + 1)
        backtrack(i + 1, cur_path)
        cur_path.pop()
        backtrack(i + 1, cur_path)
        
    backtrack(0, [])
    return res