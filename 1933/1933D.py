t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    occ_first = 1
    i = 1
    while i < n and l[i] == l[0]:
        occ_first += 1
        i += 1
    if occ_first == 1:
        p.append("YES")
    else:
        assert occ_first > 1
        exists_good = False
        for x in l:
            if x%l[0]!=0:
                exists_good = True
        if exists_good:
            p.append("YES")
        else:
            p.append("NO")
for x in p:
    print(x)