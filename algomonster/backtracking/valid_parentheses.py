def generate_parentheses(n):
    def dfs(num_left, num_right, cur_path):
        if num_left == num_right == n:
            parentheses.append(''.join(cur_path))
            return
        
        if num_left < n:
            cur_path.append('(')
            dfs(num_left + 1, num_right, cur_path)
            cur_path.pop()

        if num_right < num_left:
            cur_path.append(')')
            dfs(num_left, num_right + 1, cur_path)
            cur_path.pop()

    parentheses = []
    if n > 0: dfs(0, 0, [])
    return parentheses