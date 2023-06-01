number_to_letters = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def letter_combinations_of_phone_number(digits):
    def dfs(cur_idx, path):
        if cur_idx == len(digits):
            all_combinations.append(''.join(path))
            return
        
        for letter in number_to_letters[digits[cur_idx]]:
            path.append(letter)
            dfs(cur_idx + 1, path)
            path.pop()

    all_combinations = []
    if len(digits) > 0: dfs(0, [])
    return all_combinations