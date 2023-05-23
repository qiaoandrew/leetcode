from collections import defaultdict


def count_palindromic_subsequence(s):
    char_to_indices = defaultdict(list)
    for idx, char in enumerate(s):
        char_to_indices[char].append(idx)

    res = 0

    for char in char_to_indices:
        if len(char_to_indices[char]) < 2:
            continue

        idx_1 = char_to_indices[char][0]
        idx_2 = char_to_indices[char][-1]

        res += len(set(s[idx_1 + 1:idx_2]))

    return res
