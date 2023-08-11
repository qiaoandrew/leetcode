def spiral_order(matrix):
    x, y = -1, 0
    x_movements, y_movements = len(matrix[0]), len(matrix) - 1
    direction = 1
    res = []
    
    while x_movements and y_movements:
        for _ in range(x_movements):
            x += direction
            res.append(matrix[y][x])
        
        for _ in range(y_movements):
            y += direction
            res.append(matrix[y][x])

        direction *= -1
        x_movements -= 1
        y_movements -= 1
    
    for _ in range(x_movements):
        x += direction
        res.append(matrix[y][x])
    
    return res