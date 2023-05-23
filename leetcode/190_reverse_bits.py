def reverse_bits(n):
    res = 0
    power = 31

    while n > 0:
        res += (n & 1) << power
        n >>= 1
        power -= 1

    return res


reverse_bits(43261596)