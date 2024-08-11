t = int(input())
p = []

def majoritaire(l,x):
    for i in range(len(l)):
        if l[i] >= x and ((i+1 < n and l[i+1] >= x) or (i+2 < n and l[i+2] >= x)):
            return True
    return False

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    i = 1
    j = 10**9
    while (j-i > 0):
        m = (i+j+1)//2
        if majoritaire(l,m):
            i = m
        else:
            j = m-1
    p.append(i)


for x in p:
    print(x)