# loop through all indices, check palindrome with even and odd lengths
def longest_palindrome(s):
    res = ''
    res_len = 0

    for i in range(len(s)):
        # even length
        start, end = i, i

        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > res_len:
                res_len = end - start + 1
                res = s[start:end + 1]

            start -= 1
            end += 1

        # odd length
        start, end = i, i + 1

        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > res_len:
                res_len = end - start + 1
                res = s[start:end + 1]

            start -= 1
            end += 1

    return res
