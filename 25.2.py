for i in range(110203, 110246):
    s = 0
    num = []
    for j in range(2, i+1):
        if i % j == 0 and j % 2 == 0:
            s += 1
            num.append(j)

    if s == 4:
        print(*num)

