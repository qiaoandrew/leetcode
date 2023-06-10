def find_all_anagrams(original, check):
    check_letters = {}
    for char in check:
        check_letters[char] = check_letters.get(char, 0) + 1

    letters = {}
    anagrams = []
    left = 0
    for right in range(len(original)):
        letters[original[right]] = letters.get(original[right], 0) + 1
        if right - left + 1 > len(check):
            letters[original[left]] -= 1
            if letters[original[left]] == 0:
                letters.pop(original[left])
            left += 1
        if check_letters == letters:
            anagrams.append(left)

    return anagrams
