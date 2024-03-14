t = int(input())
p = []
for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_filtrd = set()
    b_filtrd = set()
    possible = True
    for x in a:
        if 0 < x <= k:
            a_filtrd.add(x)
    for x in b:
        if 0 < x <= k:
            b_filtrd.add(x)
    possible = True
    A = 0
    B = 0
    for x in range(1,k+1):
        if x in a_filtrd:
            if not(x in b_filtrd):
                A += 1
        else:
            if x in b_filtrd:
                B += 1
            else:
                possible = False
    if not(A <= k//2 and B<=k//2):
        possible = False


    if possible:
        p.append("YES")
    else:
        p.append("NO")
for x in p:
    print(x)