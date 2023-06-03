def combination_sum(candidates, target):
    def dfs(cur_idx, cur_sum, cur_path):
        if cur_sum == target:
            combinations.append(cur_path[:])
            return

        for i in range(cur_idx, len(candidates)):
            num = candidates[i]
            if num + cur_sum <= target:
                cur_path.append(num)
                dfs(i, cur_sum + num, cur_path)
                cur_path.pop()

    candidates.sort()
    combinations = []
    if len(candidates) > 0:
        dfs(0, 0, [])
    return combinations
