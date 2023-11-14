for i in range(174457, 174506):
    s = 0
    num = []
    for j in range(2, i//2 + 1):

        if i % j == 0:
            s += 1
            num.append(j)
    if s == 2:
        print(*num)

