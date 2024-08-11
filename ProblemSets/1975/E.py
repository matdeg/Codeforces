t = int(input())
p = []

for _ in range(t):
    n,q = map(int,input().split())
    c = list(map(int,input().split()))
    g = [[] for _ in range(n)]
    for _ in range(n-1):
        a,b = map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    black = sum(c)
    degree = 0
    for i in range(n):
        if c[i]:
            for v in g[i]:
                degree += c[v]

    print(degree)
    for _ in range(q):
        u = int(input()) - 1
        if c[u]:
            c[u] = 0
            for v in g[u]:
                if c[v]:
                    degree -= 2
        else:
            c[u] = 1
            for v in g[u]:
                if c[v]:
                    degree += 2
        print(degree)


for x in p:
    print(x)