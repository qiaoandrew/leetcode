def valid_palindrome(s):

    def helper(start, end, has_deleted):
        while start < end:
            if s[start] != s[end]:
                if has_deleted:
                    return False
                else:
                    return helper(start, end - 1, True) or helper(
                        start + 1, end, True)
            else:
                start += 1
                end -= 1

        return True

    return helper(0, len(s) - 1, False)


print(valid_palindrome('aba'))
print(valid_palindrome('abca'))
print(valid_palindrome('abc'))