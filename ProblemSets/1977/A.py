t = int(input())
p = []

for _ in range(t):
    a,b = map(int,input().split())
    if a >= b and (a-b)%2==0:
        p.append("yes")
    else:
        p.append("no")

for x in p:
    print(x)