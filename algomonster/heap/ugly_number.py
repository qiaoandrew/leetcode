from heapq import heappush, heappop


def nth_ugly_number(n):
    factors = (2, 3, 5)
    ugly_numbers = [1]
    visited = set([1])

    for _ in range(n - 1):
        num = heappop(ugly_numbers)
        for factor in factors:
            new_num = num * factor
            if new_num not in visited:
                heappush(ugly_numbers, new_num)
                visited.add(new_num)

    return ugly_numbers[0]
