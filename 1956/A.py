t= int(input())
p = []
for _ in range(t): 
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    qs = list(map(int,input().split()))
    m = min(a)
    sol = []
    for x in qs:
        sol.append(min(x,m-1))
    print(*sol)