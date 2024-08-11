t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    sol = []
    p = 1
    while 2*p-1 < k:
        sol.append(p)
        p *= 2
    # 2p-1 >= k > p-1
    if k-p > 0:
        sol.append(k-p)
    sol.append(k+1)
    couvert = 2*k
    # [1, k-1] U [k+1, 2k]
    if couvert < n:
        sol.append(2*k+1)
    # [1,k-1] U [k+1,3k] U [3k+2, 4k+1]
    couvert = 3*k
    while couvert < n:
        sol.append(couvert-k)
        couvert += couvert-k
    print(len(sol))
    print(*sol)


    
    
