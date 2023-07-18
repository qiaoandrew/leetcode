def merge_intervals(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(interval[1], merged_intervals[-1][1])
        else:
            merged_intervals.append(interval)
    return merged_intervals