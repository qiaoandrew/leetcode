def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda interval: interval[1])
    num = 0
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end:
            last_end = end
        else:
            num += 1
    
    return num