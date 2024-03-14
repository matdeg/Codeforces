t = int(input())
p = []
for _ in range(t):
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    d = list(map(int,input().split()))
    f = list(map(int,input().split()))
    d.sort()
    f.sort()
    max_length = 0
    for i in range(n-1):
        max_length = max(max_length,a[i+1] - a[i])
    max_indices = []
    for i in range(n-1):
        if a[i+1] - a[i] == max_length:
            max_indices.append(i)
    if len(max_indices) > 1:
        p.append(max_length)
    else:
        best = 0
        i0 = max_indices[0]
        # we want to insert between a[i0] + best + 1 and a[i0 + 1] - best - 1
        for i in range(m):
            d_val = d[i]

            if d_val < a[i0 + 1] - best - 1:
                
                
                left,right = 0,k-1
                while right - left > 0:
                    m = (right + left)//2
                    if f[m] + d_val >= a[i0]+best:
                        right = m
                    else:
                        left = m+1
                first = left

                left,right = 0,k-1
                while right - left > 0:
                    m = (right + left)//2
                    if f[m+1] + d_val <= a[i0+1]-best:
                        left = m+1
                    else:
                        right = m
                snd = left
                if first <= snd:
                    #from first to snd are all the values between a[i0] + best and a[i0 + 1] - best
                    for o in range(first,snd+1):
                        best = max(best, min(f[o] + d_val - a[i0],a[i0+1] - f[o] - d_val))
        diff = [a[i+1] - a[i] for i in range(n-1)]
        diff[i0] -= best
        p.append(max(diff))
for x in p:
    print(x)


                