t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    p.append(max(l)-min(l))
for x in p:
    print(x)