'''
ai + aj = mx
ai - aj = ny
2ai = mx + ny -> x^y | 2 ai
2aj = mx - ny -> x^y | 2 aj

Conversely, it doesn't work
but it is a good necessarly criter
'''

from math import gcd

t = int(input())
print_buff = []

def ans(n,x,y,tab):
    S = 0
    d = {}
    for v in tab:
        vx = v%x
        vy = v%y
        if (vx,vy) in d.keys():
            d[(vx,vy)] += 1
        else:
            d[(vx,vy)] = 1

    for v in tab:
        vmx = (-v)%x
        vy = v%y
        if (vmx,vy) in d.keys():
            S += d[(vmx,vy)]
        if v%x == (-v)%x:
            S -= 1
    print_buff.append(S//2)


for loop in range(t):
    n,x,y = map(int,input().split())
    tab = list(map(int,input().split()))
    ans(n,x,y,tab)

for x in print_buff:
    print(x)