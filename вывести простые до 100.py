def func_easy(a):
    s = True
    #for i in range(2, a//2 + 1):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            s = False
            break
    return s


for i .n range(10**9, 10**9 + 100):
    if func_easy(i): print(i)