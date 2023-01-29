def majority_element(nums):
    freq_needed = len(nums) // 2

    freqs = {}

    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1

        if freqs[num] > freq_needed:
            return num
