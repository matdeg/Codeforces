t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    max2 = 2*n - 2
    if k == 4*n - 2:
        p.append(2*n)
    elif k == 4*n - 1:
        p.append(2*n - 1)
    else:
        p.append((k+1)//2)
for x in p:
    print(x)
