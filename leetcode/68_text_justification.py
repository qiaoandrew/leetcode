from typing import List

def full_justify(words: List[str], max_width: int) -> List[str]:
    res = []
    cur_row_words = []
    cur_row_words_length = 0

    for word in words:
        if cur_row_words_length + len(cur_row_words) + len(word) > max_width:
            extra_spaces = max_width - cur_row_words_length
            space_sections = len(cur_row_words) - 1
            if space_sections > 0:
                space_distributions = [extra_spaces // space_sections] * space_sections
                for i in range(extra_spaces % space_sections):
                    space_distributions[i % space_sections] += 1

                cur_row = []
                for i in range(len(cur_row_words)):
                    cur_row.append(cur_row_words[i])
                    if i != len(cur_row_words) - 1:
                        cur_row.append(' ' * space_distributions[i])

                res.append(''.join(cur_row))
            else:
                res.append(cur_row_words[0] + ' ' * extra_spaces)
                
            cur_row_words = []
            cur_row_words_length = 0

        cur_row_words.append(word)
        cur_row_words_length += len(word)

    last_line = ' '.join(cur_row_words)
    last_line += ' ' * (max_width - len(last_line))
    res.append(last_line)

    return res