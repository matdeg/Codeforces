t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    if k >= n-1:
        p.append(1)
    else:
        p.append(n)
for x in p:
    print(x)