# Base: Carry counting system
# When base is X, called base-X numeral system
# Number on each digit carried over when it reaches X
# Weight of mth digit from right to left in integer part is X^m
# Weight of nth digit from left to right in fractional part is X^-n
# 123.45 in base-10 is: 1 * 10^2 + 2 * 10^1 + 3 * 10^0 + 4 * 10^-1 + 5 * 10^-2
# 720.5 in base-8 is: 7 * 8^2 + 2 * 8^1 + 0 * 8^0 + 5 * 8^-1

# Non-decimal to decimal
# Add weighted sum of each digit

# Decimal to non-decimal
# Convert integer part and fractional part separately
# Integer: Divide by X until it reaches 0 and record remainder each time
# Remainder in reverse order gives representation in base-X system
# Fractional: Multiply fractional part by X until it becomes 0 and record integer part each time
# Integer part in order gives representation in base-X


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


# Signed integers: Highest bit (signed bit) represents sign
# Signed bit is 0, non-negative integer
# Signed bit is 1, negative integer
# Digits other than highest bit represent size of number
# Range is -2^k-1 to 2^k-1 - 1 where k is number of bits

# Unsigned integer: Cannot represent negative numbers
# Range is 0 to 2^k - 1

# Machine number: Binary representation of number in computer
# Signed number, highest bit is sign bit
# +10 is 00001010 in binary
# -10 is 10001010 in binary
# Since highest bit is sign bit, value of machine number is not necessarily equal to true value
# 10001010 is 138 as a decimal number, but truth value is -10

# Original code: Sign bit of machine number plus absolute value of truth value of machine number
# Has dual representation of 0 problem
# Performing subtractions with original code leads to incorrect

# Inverse code: Same as original code for non-negative, flip every bit except sign bit for negative
# Fixes subtraction error, still has dual representation error

# Complement code: Same as original and inverse code for non-negative, add 1 to inverse code for negative
# Fixes dual representation error

# Bit operations

# AND (&)
# For every binary bit, when corresponding bits of both number are 1, result is 1, otherwise 0

# OR (|)
# When both are 0, result is 0, otherwise 1

# XOR (^)
# When bits are same, result is 0, otherwise 1

# Negation (~)
# Flip bit of number

# Left shift (<<)
# Bits shifted to left by several bits, high bits discarded, low bits filled with 0
# Arithmetic shift and logical shit are same

# Right shift (>>)
# Bits shifted to right by several bits, low bits discarded
# Arithmetically, high bits filled with highest bit
# Logically, high bits filled with 0
# For non-negative numbers, arithmetic right shift and logical right shift are identical

# For signed types, right shift is arithmetic right shift
# For unsigned types, right shift is logical right shift

# Shift operations related closely to multiplication and division
# Efficiency of shift multiplication/division is higher than regular

# Shifting left by k bits is same as multiplying by 2^k
# When multiplier is not integer power of 2, multiplier can be split into sum of integer powers of 2
# a * 6 is equivalent to ( a << 2 ) + ( a << 1 )

# Shifting right by k bits is same as dividing by 2^k for non-negative numbers
# Not the same for negative numbers

# Properties of bitwise operations
# Idempotent law: a & a = a, a | a = a
# Commutative law: a & b = b & a, a | b = b | a, a ^ b = b ^ a
# Associativity: (a & b) & c = a & (b & c), (a | b) | c = a | (b | c), (a ^ b) ^ c = a ^ (b ^ c)
# Distributive law: (a & b) | c = (a | c) & (b | c), (a | b) & c = (a & c) | (b & c), (a ^ b) & c = (a & c) ^ (b & c)
# De Morgan's law: ~(a & b) = (∼a) | (∼b), ∼(a | b) = (∼a) & (∼b)
# Negative operation properties: -1 = ∼0, -a = ∼(a − 1)
# AND operation properties: a & 0 = 0, a & (-1) = a, a & (∼a) = 0
# OR operation properties: a | 0 = a, a | (∼a) = −1
# XOR operation properties: a ^ 0 = a, a ^ a = 0
# Other properties:
# Result of a & (a - 1) is change last 1 in binary representation of a to 0
# Result of a & (-a) is keep only last 1 of binary representation of a and set remaining 1s to 0