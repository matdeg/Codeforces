t = int(input())
p = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    def test(i):
        ok = True
        for j in range(n-i):
            if a[j] > b[i+j]:
                ok = False
        return ok
    
    i = 0
    while i < n and not(test(i)):
        i += 1
    p.append(i)
for x in p:
    print(x)