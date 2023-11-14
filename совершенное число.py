s = 0
for i in range(1, (a := int(input()))):
    if a % i == 0:
        s += i
if s == a: print('СОВЕРШЕНОЕ')
else: print('НЕ СОВЕРШЕННОЕ')