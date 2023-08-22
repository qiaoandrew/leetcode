def convert_to_title(column_number):
    col_title = []
    while column_number:
        column_number -= 1
        col_title.append(chr(column_number % 26 + ord('A')))
        column_number //= 26
    return ''.join(reversed(col_title))