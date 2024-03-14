t = int(input())
pbuff = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    i = 0
    j = 0
    best = 1
    current = 1
    while j < n-1:
        while j < n-1 and l[j+1] - l[i] <= n-1:
            if l[j+1] != l[j]:
                current += 1
                best = max(best,current)
            j += 1
        while j < n-1 and l[j+1] - l[i] > n-1:
            if l[i+1] != l[i]:
                current -= 1
            i += 1
    pbuff.append(best)

for x in pbuff:
    print(x)

    

    
    
