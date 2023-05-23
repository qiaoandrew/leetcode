def convert_to_base_7(num):
    if num == 0:
        return '0'

    is_negative = False

    if num < 0:
        num *= -1
        is_negative = True

    remainders = []

    while num > 0:
        remainders.append(str(num % 7))
        num = num // 7

    if is_negative:
        return '-' + ''.join(reversed(remainders))
    else:
        return ''.join(reversed(remainders))
