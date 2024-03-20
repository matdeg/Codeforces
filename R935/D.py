t = int(input())
p = []
for _ in range(t):
    n,m = map(int,input().split())
    a_rev = list(map(int,input().split()))
    b_rev = list(map(int,input().split()))
    a = [a_rev[n-i-1] for i in range(n)]
    b = [b_rev[n-i-1] for i in range(n)]

    glutto = [min(a[0],b[0])]
    for i in range(1,n):
        glutto.append(glutto[-1] + min(a[i],b[i]))
    best = []
    best.append(a[0])
    for i in range(1,n):
        best.append(a[i] + glutto[i-1])
    mini = float("inf")
    for i in range(n-m,n):
        if best[i] < mini:
            mini = best[i]
    p.append(mini)
for x in p:
    print(x)


'''

4 2
7 3 6 9
4 3 8 5


7 7 13 
'''