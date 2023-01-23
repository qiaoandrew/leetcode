def count_palindromes(s):
    res = 0

    for i in range(len(s)):
        # odd length
        start, end = i, i

        while start >= 0 and end < len(s) and s[start] == s[end]:
            res += 1

            start -= 1
            end += 1

        # even length
        start, end = i, i + 1

        while start >= 0 and end < len(s) and s[start] == s[end]:
            res += 1

            start -= 1
            end += 1

    return res