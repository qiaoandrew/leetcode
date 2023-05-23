def newspapers_split(newspapers_read_times, num_coworkers):
    def feasible(time_per_worker):
        workers_needed = 1
        time_left_for_current_worker = time_per_worker

        for newspaper_time in newspapers_read_times:
            if newspaper_time > time_left_for_current_worker:
                workers_needed += 1
                time_left_for_current_worker = time_per_worker

                if workers_needed > num_coworkers:
                    return False
            
            time_left_for_current_worker -= newspaper_time
        
        return True

    left, right = max(newspapers_read_times), sum(newspapers_read_times)
    feasible_boundary = -1

    while left <= right:
        mid = left + (right - left) // 2
        if feasible(mid):
            feasible_boundary = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return feasible_boundary