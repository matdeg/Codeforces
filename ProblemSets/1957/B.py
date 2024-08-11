t = int(input())

for _ in range(t):
    sol = []
    n,k = map(int,input().split())
    p = 1
    while p <= k:
        p = 2*p + 1
    p = (p-1)//2
    if n >= 2:
        print(p,k-p,end=" ")
        for _ in range(n-2):
            print(0,end=" ")
    else:
        # n = 1
        print(k)
    

    