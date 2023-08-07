def can_attend_meetings(intervals):
    intervals.sort(key=lambda interval: interval[0])
    for i in range(1, len(intervals)):
        prev, cur = intervals[i - 1], intervals[i]
        if cur[0] < prev[1]:
            return False
    return True