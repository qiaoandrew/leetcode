def longest_substring_without_repeating_characters(s):
    longest = 0
    count = {}
    left = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1
        while count[s[right]] > 1:
            count[s[left]] -= 1
            left += 1
        longest = max(longest, right-left+1)
    return longest
