def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def partition(s):
    def dfs(start_idx, path):
        if start_idx >= len(s):
            partitions.append(path[:])
            return

        for end_idx in range(start_idx, len(s)):
            if is_palindrome(s[start_idx:end_idx + 1]):
                path.append(s[start_idx:end_idx + 1])
                dfs(end_idx + 1, path)
                path.pop()
    
    partitions = []
    if len(s) > 0: dfs(0, [])
    return partitions

print(partition('aab'))