def get_skyline(buildings):
    def get_skyline_helper(buildings):
        def merge(left, right):
            def update(x, y):
                if not result or (result[-1][0] != x and result[-1][1] != y):
                    result.append([x, y])
                else:
                    result[-1][1] = y
            
            result = []
            i1, i2 = 0, 0
            ly, ry = 0, 0

            while i1 < len(left) and i2 < len(right):
                x1, y1 = left[i1]
                x2, y2 = right[i2]
                if x1 < x2:
                    i1 += 1
                    ly = y1
                else:
                    i2 += 1
                    ry = y2
                curx = min(x1, x2)
                cury = max(ly, ry)
                update(curx, cury)

            while i1 < len(left):
                x1, y1 = left[i1]
                i1 += 1
                update(x1, y1)
            
            while i2 < len(right):
                x2, y2 = right[i2]
                i2 += 1
                update(x2, y2)
            
            return result

        length = len(buildings)
        if length == 0:
            return []
        elif length == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        left_skyline = get_skyline_helper(buildings[:length//2])
        right_skyline = get_skyline_helper(buildings[length//2:]) 
        return merge(left_skyline, right_skyline)

    return get_skyline_helper(buildings)

print(get_skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))