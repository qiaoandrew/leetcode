def arrange_coins(n):
    res = 0
    cur_row_length = 1

    while n >= cur_row_length:
        n -= cur_row_length
        cur_row_length += 1
        res += 1

    return res


print(arrange_coins(5))