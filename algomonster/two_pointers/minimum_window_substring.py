def get_minimum_window(original, check):
    check_count = {}
    for char in check:
        check_count[char] = check_count.get(char, 0) + 1

    letters_complete = 0
    letters_complete_needed = len(check_count)
    window_count = {}
    min_substring = ''
    min_substring_len = float('inf')
    left = 0

    for right in range(len(original)):
        char = original[right]
        if not char in check_count:
            continue
        window_count[char] = window_count.get(char, 0) + 1
        if window_count[char] == check_count[char]:
            letters_complete += 1
        while letters_complete == letters_complete_needed:
            if right - left + 1 < min_substring_len or (right - left + 1 == min_substring_len and original[left: right + 1] < min_substring):
                min_substring = original[left: right + 1]
                min_substring_len = right - left + 1
            left_char = original[left]
            if left_char in check_count:
                window_count[left_char] -= 1
                if window_count[left_char] == check_count[left_char] - 1:
                    letters_complete -= 1
            left += 1

    return min_substring


print(get_minimum_window('cdbaebaecd', 'abc'))
