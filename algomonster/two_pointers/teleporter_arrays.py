MODULO_AMT = 10 ** 9 + 7


def maximum_score(arr1, arr2):
    ans = 0
    p1, p2 = 0, 0
    sum1, sum2 = 0, 0
    len1, len2 = len(arr1), len(arr2)

    while p1 < len1 or p2 < len2:
        if p1 == len1:
            sum2 += arr2[p2]
            p2 += 1
        elif p2 == len2:
            sum1 += arr1[p1]
            p1 += 1
        elif arr2[p2] < arr1[p1]:
            sum2 += arr2[p2]
            p2 += 1
        elif arr1[p1] < arr2[p2]:
            sum1 += arr1[p1]
            p1 += 1
        else:
            ans += max(sum1, sum2)
            ans %= MODULO_AMT
            sum1, sum2 = arr1[p1], arr2[p2]
            p1 += 1
            p2 += 1

    ans += max(sum1, sum2)
    ans %= MODULO_AMT
    return ans
