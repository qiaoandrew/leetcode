def insert_interval(intervals, new_interval):
    if len(intervals) == 0:
        return [new_interval]
    merged_intervals = []
    for i in range(len(intervals)):
        interval = intervals[i]
        if interval[0] > new_interval[1] or new_interval[0] > interval[1]:
            merged_intervals.append(interval)
        else:
            merged_interval = [min(interval[0], new_interval[0]), max(interval[1], new_interval[1])]
            if len(merged_intervals) > 0 and merged_intervals[-1][1] >= merged_interval[0]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], merged_interval[1])
            else:
                merged_intervals.append(merged_interval)
    return merged_intervals

print(insert_interval([[1,3],[6,9]], [2,5]))
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(insert_interval([], [5,7]))
print(insert_interval([[1,5]], [2,3]))
print(insert_interval([[1,5]], [2,7]))
