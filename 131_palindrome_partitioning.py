def partition(s):
    res = []

    cur_partition = []

    def is_palindrome(s, start, end):

        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def dfs(i):
        if i == len(s):
            res.append(cur_partition[:])
            return

        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                cur_partition.append(s[i:j + 1])

                dfs(j + 1)

                cur_partition.pop()

    dfs(0)

    return res


print(partition('aab'))