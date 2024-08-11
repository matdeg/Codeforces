t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    exists2 = 0
    exists1 = 0
    for x in l:
        if x%3 == 1:
            exists1 += 1
        if x%3 == 2:
            exists2 += 1
    targ = sum(l)%3
    if targ == 2:
        p.append(1)
    elif targ == 0:
        p.append(0)
    else:
        assert targ == 1
        if exists1 > 0:
            p.append(1)
        else:
            p.append(2)
for x in p:
    print(x)