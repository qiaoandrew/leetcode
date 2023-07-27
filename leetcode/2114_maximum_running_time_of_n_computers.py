class BinarySearchSolution:
    def max_run_time(self, n, batteries):
        left, right = 1, sum(batteries) // n
        boundary = -1

        while left <= right:
            target = left + (right - left) // 2

            total_power = 0
            for battery in batteries:
                total_power += min(battery, target)
            
            if total_power // n >= target:
                left = target + 1
                boundary = target
            else:
                right = target - 1
        
        return boundary