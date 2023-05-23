def min_swaps(s):
    open_brackets = 0
    ans = 0

    for bracket in s:
        if bracket == ']':
            if open_brackets > 0:
                open_brackets -= 1
            else:
                open_brackets += 1
                ans += 1
        else:
            open_brackets += 1

    return ans
