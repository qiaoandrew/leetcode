def min_meeting_rooms(intervals):
    start_times = sorted(interval[0] for interval in intervals)
    end_times = sorted(interval[1] for interval in intervals)

    rooms = 0

    start_pointer = 0
    end_pointer = 0

    while start_pointer < len(intervals):
        if start_times[start_pointer] >= end_times[end_pointer]:
            rooms -= 1
            end_pointer += 1

        rooms += 1
        start_pointer += 1

    return rooms