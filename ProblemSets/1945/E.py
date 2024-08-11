t = int(input())
for test in range(t):
    n,x = map(int,input().split())
    perm = list(map(int,input().split()))
    ix = -1
    for i in range(n):
        if perm[i] == x:
            ix = i

    l = 1
    r = n+1
    while r - l != 1:
        m = (r+l)//2
        if perm[m-1] <= x:
            l = m
        else:
            r = m
    if perm[l-1] == x:
        print(0)
    else:
        perm[ix],perm[l-1] = perm[l-1],perm[ix]
        l2 = 1
        r2 = n+1
        while r2 - l2 > 1:
            m = (r2+l2)//2
            if perm[m-1] <= x:
                l2 = m
            else:
                r2 = m
        if perm[l2-1] == x:
            print(1)
            print("{} {}".format(ix+1,l))
        else:
            print("aie")

