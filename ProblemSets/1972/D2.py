import math
t = int(input())

for a in range(1,t):
    for b in range(1,t):
        if (b * math.gcd(a,b))%(a+b)==0:
            d = math.gcd(a,b)
            aa = a//d
            bb = b//d
            print(a,b)