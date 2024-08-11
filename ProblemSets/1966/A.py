t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    occ = [0] * 102
    for x in l:
        occ[x] += 1
    ex = False
    for x in occ:
        if x >= k:
            ex = True
    if ex:
        p.append(k-1)
    else:
        p.append(n)
for x in p:
    print(x)