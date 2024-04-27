t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    occ = [0] * 200
    for x in l:
        occ[x] += 1
    s = 0
    for x in occ:
        s += x//3
    p.append(s)
for x in p:
    print(x)