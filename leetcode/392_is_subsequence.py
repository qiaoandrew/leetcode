def is_subsequence(s, t):
    s_pointer = 0

    for char in t:
        if s_pointer == len(s):
            break

        if s[s_pointer] == char:
            s_pointer += 1

    return s_pointer == len(s)


print(is_subsequence('abc', 'ahbgdc'))
print(is_subsequence('axc', 'ahbgdc'))