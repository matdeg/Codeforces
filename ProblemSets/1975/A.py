t = int(input())
p = []

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    s = 0
    for i in range(n):
        if l[i] > l[(i+1)%n]:
            s += 1
    if s <= 1:
        p.append("yes")
    else:
        p.append("no")

for x in p:
    print(x)