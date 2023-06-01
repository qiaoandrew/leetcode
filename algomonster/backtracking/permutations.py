def permutations(letters):
    def dfs(used_letters, cur_path):
        if len(used_letters) == len(letters):
            all_permutations.append(''.join(cur_path))
            return

        for letter in letters:
            if letter not in used_letters:
                cur_path.append(letter)
                used_letters.add(letter)
                dfs(used_letters, cur_path)
                cur_path.pop()
                used_letters.remove(letter)

    all_permutations = []
    if len(letters) > 0: dfs(set(), [])
    return all_permutations