from collections import defaultdict


def group_anagrams(strs):
    anagrams = defaultdict(list)

    for string in strs:
        anagrams[''.join(sorted(list(string)))].append(string)

    res = []

    for group in anagrams.values():
        res.append(group)

    return res
