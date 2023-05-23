def letter_combinations(digits):
    if len(digits) == 0:
        return []

    digit_to_letter = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }

    res = []

    cur_combination = []

    def dfs(i):
        if i == len(digits):
            res.append(''.join(cur_combination))
            return

        for letter in digit_to_letter[digits[i]]:
            cur_combination.append(letter)

            dfs(i + 1)

            cur_combination.pop()

    dfs(0)

    return res
