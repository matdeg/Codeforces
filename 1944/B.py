t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    t = list(map(int,input().split()))
    tab = [0] * (n+1)
    for i in range(n):
        tab[t[i+n]] += 1
    # left = 0
    # both = 1
    # right = 2
    left = []
    right = []
    both = []
    for i in range(1,n+1):
        if tab[i] == 0:
            left.append(i)
        elif tab[i] == 1:
            both.append(i)
        else:
            right.append(i)
    to_take = 2*k
    l = []
    r = []
    for i in range(min(2*(len(both)//2),2*k)):
        x = both[i]
        l.append(x)
        r.append(x)
        to_take -= 1
    for i in range(len(left)):
        if to_take > 0:
            l.append(left[i])
            l.append(left[i])
            r.append(right[i])
            r.append(right[i])
            to_take -= 2
    for x in l:
        print(x,end = " ")
    print()
    for x in r:
        print(x,end = " ")
    print()
    



