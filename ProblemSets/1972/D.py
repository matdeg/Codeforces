t = int(input())
p = []
for _ in range(t):
    n,m = list(map(int,input().split()))
    s = 0
    for b in range(1,m+1):
        s += (n+b)//(b**2)
    p.append(s)
for x in p:
    print(x-1)