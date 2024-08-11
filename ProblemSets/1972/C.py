t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    l.sort()

    def manque(target):
        i = 0
        s = 0
        while i < n and l[i] < target:
            s += (target - l[i])
            i += 1
        return s

    i,j = 0,2*10**12
    while j-i > 0:
        m = (i+j+1)//2
        manq = manque(m)
        if manq > k:
            j = m-1
        elif manq == k:
            i = m
            j = m
        else:
            i = m
    
    target = max(i,min(l))
    assert manque(target) <= k and manque(target+1) > k
    for i in range(n):
        if l[i] < target:
            k -= (target - l[i])
            l[i] = target
    count_target = 0
    for x in l:
        if x == target:
            count_target += 1
    count_target -= k
    k = 0
    p.append((target-1) * n + 1 + (n-count_target))

for x in p:
    print(x)