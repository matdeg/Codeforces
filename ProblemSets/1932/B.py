t = int(input())
p = []


def aux(a,b):
    # return smallest multiple of b greater (strictly) than a
    #    kb > a >= (k-1)b 
    # k = (a + b + 1)/b

    return ((a+b)//b)*b

for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    x = l[0] 
    for i in range(1,n):
        x = aux(x,l[i])
    p.append(x)
for x in p:
    print(x)