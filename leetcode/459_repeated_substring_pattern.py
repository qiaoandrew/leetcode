def repeated_substring_pattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        pattern_repeated = s[:i] * (n // i)
        if pattern_repeated == s:
            return True
    return False