from math import lcm, sqrt

t = int(input())
p = []

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    LCM = lcm(*l)
    if LCM > max(l):
        p.append(n)
    else:
        best = 0
        factors = []
        for div in range(1,int(sqrt(LCM)) + 1):
            if LCM%div==0:
                factors.append(div)
                factors.append(LCM//div)
        for factor in factors:
            if factor not in l:
                divs = []
                for x in l:
                    if factor%x==0:
                        divs.append(x)
                if lcm(*divs) == factor:
                    best = max(best,len(divs))
        p.append(best)

for x in p:
    print(x)