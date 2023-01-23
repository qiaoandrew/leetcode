def length_of_last_word(s):
    end = len(s) - 1

    while s[end] == ' ':
        end -= 1

    start = end

    while s[start - 1] != ' ' and start >= 1:
        start -= 1

    return end - start + 1


print(length_of_last_word('Hello World'))
print(length_of_last_word("   fly me   to   the moon  "))
print(length_of_last_word("luffy is still joyboy"))
print(length_of_last_word('s'))
print(length_of_last_word('day'))