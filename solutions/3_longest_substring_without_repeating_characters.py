def length_of_longest_substring(s):
    res = 0

    count = {}

    left = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        while count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)

    return res


print(length_of_longest_substring('abcabcbb'))