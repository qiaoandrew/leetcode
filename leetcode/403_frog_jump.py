def can_cross(stones):
    n = len(stones)

    dp = { stone: set() for stone in stones }
    dp[0].add(0)

    for stone_idx in range(n):
        for prev_jump in dp[stones[stone_idx]]:
            for jump in range(prev_jump - 1, prev_jump + 2):
                if jump > 0 and stones[stone_idx] + jump in dp:
                    dp[stones[stone_idx] + jump].add(jump)

    return len(dp[stones[-1]]) > 0