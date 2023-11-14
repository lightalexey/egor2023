num = []
for i in range(0, 10**10 + 1, 2024):
    si = str(i)
    if si[0] == '1' and si[2:6] == '2157' and si[-1] == '4': print(i, i//2024)