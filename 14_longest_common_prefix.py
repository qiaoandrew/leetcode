def longest_common_prefix(strs):
    end = 0

    while True:
        if len(strs[0]) > end:
            char = strs[0][end]
        else:
            return strs[0][:end]

        for string in strs:
            if len(string) <= end or string[end] != char:
                return strs[0][:end]

        end += 1


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
