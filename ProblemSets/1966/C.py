t = int(input())
p = []
for _ in range(t): 
    n = int(input())
    laux = list(map(int,input().split()))
    laux.sort()
    l = [laux[0]]
    for x in laux:
        if x != l[-1]:
            l.append(x)
    n = len(l)
    for i in range(n-1,0,-1):
        l[i] = l[i] - l[i-1]
    gagne = True
    for i in range(n-2,-1,-1):
        if l[i] == 1:
            gagne = not(gagne)
        else:
            gagne = True
    if gagne:
        p.append("Alice")
    else:
        p.append("Bob")
for x in p:
    print(x)
    
