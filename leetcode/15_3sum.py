def three_sum(numbers):
    res = []

    numbers.sort()

    for num1_idx in range(len(numbers)):
        if num1_idx > 0 and numbers[num1_idx] == numbers[num1_idx - 1]:
            continue
        num1 = numbers[num1_idx]

        num2_idx = num1_idx + 1
        num3_idx = len(numbers) - 1

        while num2_idx < num3_idx:
            num2 = numbers[num2_idx]
            num3 = numbers[num3_idx]

            cur_sum = num1 + num2 + num3

            if cur_sum == 0:
                res.append([num1, num2, num3])
                num2_idx += 1
                num3_idx -= 1
            elif cur_sum > 0:
                num3_idx -= 1
            else:
                num2_idx += 1

    return res


print(three_sum([-1, 0, 1, 2, -1, -4]))
