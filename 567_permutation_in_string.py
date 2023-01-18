def check_inclusion(s1, s2):
    s1_count = {}

    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1

    s2_count = {}

    left = 0

    for right in range(len(s2)):
        s2_count[s2[right]] = s2_count.get(s2[right], 0) + 1

        if right - left + 1 == len(s1):
            if s1_count == s2_count:
                return True

            s2_count[s2[left]] -= 1

            if s2_count[s2[left]] == 0:
                s2_count.pop(s2[left])

            left += 1

    return False


print(check_inclusion('ab', 'eidbaooo'))