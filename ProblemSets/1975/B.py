t = int(input())
p = []

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    acc = []
    for x in l: 
        add = True
        for y in acc:
            if x%y == 0:
                add = False
        if add:
            acc.append(x)
        
    if len(acc) <= 2:
        p.append("yes")
    else:
        p.append("no")
for x in p:
    print(x)