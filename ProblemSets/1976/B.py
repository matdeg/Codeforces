def distance(x,a,b):
    if a <= x <= b:
        return 0
    if b <= x <= a:
        return 0
    return min(abs(x-a),abs(x-b))

t = int(input())
p = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    s = 0
    last = b[-1]
    best = float('inf')
    for i in range(n):
        s += abs(a[i]-b[i])
        best = min(best, distance(last,a[i],b[i]))
    s += best + 1
    p.append(s)
for x in p:
    print(x)