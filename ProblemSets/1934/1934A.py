t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    a,b,c,d = l[0],l[1],l[-2],l[-1]
    v = (d-a) + (c-a) + (d-b) + (c-b)
    p.append(v)
for x in p:
    print(x)