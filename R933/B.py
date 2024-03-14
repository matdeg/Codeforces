t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(n-2):
        a = l[i] 
        if a > 0:
            l[i+1] -= 2*a
            l[i+2] -= a
            l[i] -= a
    possible = True
    for i in range(n):
        if l[i] != 0:
            possible = False
    p.append(possible)

for x in p:
    if x:
        print("YES")
    else:
        print("NO")

    