# dfs
def partition(s):
    res = []
    cur = []

    def is_palindrome(start, end):
        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    def dfs(i):
        if i == len(s):
            res.append(cur[:])
            return

        for j in range(i, len(s)):
            if is_palindrome(i, j):
                cur.append(s[i:j + 1])

                dfs(j + 1)

                cur.pop()

    dfs(0)

    return res