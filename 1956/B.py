t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    occ = [0] * n
    for x in l:
        occ[x-1] += 1
    s = 0
    for x in occ:
        s += (x == 2)
    p.append(s)
for x in p:
    print(x)