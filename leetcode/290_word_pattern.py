def word_pattern(pattern, s):
    words = s.split(' ')

    if len(pattern) != len(words):
        return False

    letter_to_word = {}
    word_to_letter = {}

    for i in range(len(pattern)):
        letter = pattern[i]
        word = words[i]

        if letter in letter_to_word and letter_to_word[letter] != word:
            return False

        if word in word_to_letter and word_to_letter[word] != letter:
            return False

        letter_to_word[letter] = word
        word_to_letter[word] = letter

    return True


print(word_pattern('abba', 'dog cat cat dog'))
print(word_pattern('abba', 'dog cat cat fish'))
print(word_pattern('aaaa', 'dog cat cat dog'))