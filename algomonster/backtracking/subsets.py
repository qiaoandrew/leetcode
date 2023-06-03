def subsets(nums):
    def dfs(cur_idx, cur_path):
        if cur_idx == len(nums):
            res.append(cur_path[:])
            return

        cur_path.append(nums[cur_idx])
        dfs(cur_idx + 1, cur_path)
        cur_path.pop()

        dfs(cur_idx + 1, cur_path)

    res = []
    if len(nums) > 0:
        dfs(0, [])
    return res


print(subsets([1, 2, 3]))
