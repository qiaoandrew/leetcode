def max_number_of_balloons(text):
    letters = {'b', 'a', 'l', 'o', 'n'}

    letter_freq = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

    for char in text:
        if char in letters:
            letter_freq[char] += 1

    letter_freq['l'] //= 2
    letter_freq['o'] //= 2

    res = float('inf')

    for freq in letter_freq.values():
        res = min(res, freq)

    return res


print(max_number_of_balloons('nlaebolko'))
print(max_number_of_balloons('loonbalxballpoon'))
print(max_number_of_balloons('leetcode'))