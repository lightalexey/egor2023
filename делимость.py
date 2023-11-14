s = 0
for i in range(1, (a := int(input())) + 1):
    if a % i == 0:
        print(i, end=' ')
        s += 1
print()
print(s)