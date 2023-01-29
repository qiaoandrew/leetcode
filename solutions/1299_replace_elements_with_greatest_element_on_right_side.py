def replace_elements(arr):
    res = [-1] * len(arr)
    running_greatest = arr[-1]

    for i in range(len(arr) - 2, -1, -1):
        res[i] = running_greatest
        running_greatest = max(arr[i], running_greatest)

    return res


print(replace_elements([17, 18, 5, 4, 6, 1]))
print(replace_elements([400]))