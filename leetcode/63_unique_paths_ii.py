def unique_paths_with_obstacles(obstacle_grid):
    rows, cols = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        if obstacle_grid[i][0] == 0:
            dp[i][0] = 1
        else:
            break
    
    for i in range(cols):
        if obstacle_grid[0][i] == 0:
            dp[0][i] = 1
        else:
            break
    
    for row in range(1, rows):
        for col in range(1, cols):
            if obstacle_grid[row][col] == 1:
                continue
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    
    return dp[-1][-1]