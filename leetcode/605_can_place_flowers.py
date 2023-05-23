def can_place_flowers(flowerbed, n):

    for i in range(len(flowerbed)):
        if flowerbed[i] == 1:
            continue

        if i == 0:
            if (len(flowerbed) > 1
                    and flowerbed[i + 1] == 0) or len(flowerbed) == 1:
                flowerbed[i] = 1
                n -= 1
        elif i == len(flowerbed) - 1:
            if flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
        else:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

    return n <= 0


print(can_place_flowers([1, 0, 0, 0, 1], 1))
print(can_place_flowers([1, 0, 0, 0, 1], 2))
