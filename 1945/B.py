t = int(input())
p = []
from math import gcd
for _ in range(t):
    a,b,m = map(int,input().split())
    if a > b:
        a,b = b,a

    # a <= b
    f1 = m//a
    m1 = m%a
    m2 = m%b
    f2 = m//b 
    
    f = f1 + f2
    p.append(f+2)
for x in p:
    print(x)

''' 
3 4 10

0 0 X X X 2X 2X 2X 3X 3X 3X 4X 4X 3X
0 0 0 X X X X X X X X X X

'''