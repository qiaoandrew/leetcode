class BruteForceSolution:
    def get_skyline(self, buildings):
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        edge_index_map = {x: i for i, x in enumerate(positions)}

        heights = [0] * len(positions)
        for left, right, height in buildings:
            left_idx = edge_index_map[left]
            right_idx = edge_index_map[right]
            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], height)
        
        answer = []
        for i in range(len(heights)):
            cur_height = heights[i]
            cur_x = positions[i]
            if not answer or answer[-1][1] != cur_height:
                answer.append([cur_x, cur_height])
        
        return answer
    
class DivideAndConquerSolution:
    def get_skyline(self, buildings):
        def get_skyline_helper(buildings):
            def merge(left, right):
                def update(x, y):
                    if not result or (x != result[-1][0] and y != result[-1][1]):
                        result.append([x, y])
                    else:
                        result[-1][1] = y

                result = []
                i_l, i_r = 0, 0
                y_l, y_r = 0, 0

                while i_l < len(left) and i_r < len(right):
                    x1, y1 = left[i_l]
                    x2, y2 = right[i_r]
                    if x1 < x2:
                        i_l += 1
                        y_l = y1
                    else:
                        i_r += 1
                        y_r = y2
                    cur_x = min(x1, x2)
                    cur_y = max(y_l, y_r)
                    update(cur_x, cur_y)
                
                while i_l < len(left):
                    x1, y1 = left[i_l]
                    i_l += 1
                    update(x1, y1)
                
                while i_r < len(right):
                    x2, y2 = right[i_r]
                    i_r += 1
                    update(x2, y2)
                
                return result

            length = len(buildings)
            if length == 0:
                return []
            elif length == 1:
                return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
            left_skyline = get_skyline_helper(buildings[:length // 2])
            right_skyline = get_skyline_helper(buildings[length // 2:])
            return merge(left_skyline, right_skyline)

        return get_skyline_helper(buildings)