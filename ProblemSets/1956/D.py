n = int(input())
l = list(map(int,input().split()))
p = []
def to_zero(i,j):
    for x in range(i-1,j):
        if l[x] != 0:
            p.append((x+1,x+1))
            l[x] = 0

def escaliers(i,j):
    if i == j:
        to_zero(i,j)
    else:
        to_zero(i,j)
        escaliers(i+1,j)
        p.append((i+1,j))
        for k in range(i,j):
            l[k] = j-i
        to_zero(i,j-1)
        escaliers(i,j-1)

def best(i,j):
    escaliers(i,j)
    p.append((i,j))
    for k in range(i-1,j):
        l[k] = j-i+1

for lg in range(n,0,-1):
    for i in range(n-lg+1):
        j = i + lg - 1
        s = 0
        for k in range(i,j+1):
            s += l[k]
        if s < lg * lg:
            best(i+1,j+1)

print(sum(l),len(p))
for a,b in p:
    print(a,b)