a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4*a*c
if D == 0:
    print(f"x1=x2={-b/(2*a)}")
elif D < 0:
    print("действительных Корней нет")
else:
    print(f"x1={(-b + D**0.5)/2/a}, x2={(-b - D**0.5)/2/a}")
