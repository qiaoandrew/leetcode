def generate_parenthesis(n):
    res = []

    parenthesis = []

    def dfs(num_open, num_closed):
        if num_closed == n:
            res.append(''.join(parenthesis))
            return

        if num_open < n:
            parenthesis.append('(')
            dfs(num_open + 1, num_closed)
            parenthesis.pop()

        if num_closed < num_open:
            parenthesis.append(')')
            dfs(num_open, num_closed + 1)
            parenthesis.pop()

    dfs(0, 0)

    return res


print(generate_parenthesis(3))
