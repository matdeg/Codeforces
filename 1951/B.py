t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    cows = list(map(int,input().split()))
    score = cows[k-1]
    first_better = k-1
    for i in range(k-1):
        if i != k-1 and first_better == k-1 and cows[i] > score:
            first_better = i
    
    cows[0],cows[k-1] = cows[k-1],cows[0]
    before = 0
    i = 1
    while i < n and cows[i] < score:
        before += 1
        i += 1

    cows[0],cows[k-1] = cows[k-1],cows[0]
    cows[first_better],cows[k-1] = cows[k-1],cows[first_better]

    i = first_better + 1
    after = int(first_better > 0) 
    while i < n and (cows[i] < score):        
        after += 1
        i += 1
    p.append(max(before,after))
for x in p:
    print(x)
