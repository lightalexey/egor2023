for j in range(1, 10**9):
    s = 0
    for i in range(1, j//2+1):
        if j % i == 0:
            s += i
    if s == j:
        print(j, bin(j)[2:])


