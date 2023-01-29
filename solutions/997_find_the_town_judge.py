def find_judge(n, trust):
    # (number of ppl that person trusts, number of ppl that trusts person)
    trusts = {i: [0, 0] for i in range(1, n + 1)}

    for a, b in trust:
        trusts[a][0] += 1
        trusts[b][1] += 1

    for person in range(1, n + 1):
        if trusts[person][0] == 0 and trusts[person][1] == n - 1:
            return person

    return -1


print(find_judge(3, [[1, 3], [2, 3]]))
