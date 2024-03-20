t = int(input())
p = []
for _ in range(t):
    n,m,k = map(int,input().split())
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    
    s = 0
    for x in l1:
        for y in l2:
            if x + y <= k:
                s += 1
    p.append(s)
for x in p:
    print(x)