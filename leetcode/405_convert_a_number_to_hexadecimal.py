# 1 digit hexadecimal number corresponds to 4 digit binary number
# int can be represented as 32 bit binary number or 8 bit hexadecimal number
# Convert integer to binary number and then to hexadecimal number in groups of four digits


# Binary digits divided into 8 groups of 4
# Each group converted into corresponding hexadecimal numbers, concatenated into hexadecimal number
def to_hex(num):
    if num == 0:
        return '0'

    hexadecimal = '0123456789abcdef'
    res = []

    while num != 0 and len(res) < 8:
        res.append(hexadecimal[num & 15])
        num >>= 4

    return ''.join(reversed(res))