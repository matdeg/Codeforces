t = int(input())
p = []

WHITE = 0
RED = 1
BLUE = 2

for _ in range(t):
    n = int(input())
    g = [[] for _ in range(n)]
    parent = [-1] * n
    h = [-1] * n
    A,B = map(lambda x: int(x) -1,input().split())
    for _ in range(n-1):
        x,y = map(lambda x: int(x) -1,input().split())
        g[x].append(y)
        g[y].append(x)

    to_see = [0]
    parent[0] = 0
    h[0] = 0
    while to_see != []:
        u = to_see.pop()
        for v in g[u]:
            if parent[v] == -1:
                parent[v] = u
                h[v] = h[u] + 1
                to_see.append(v)

    

    
    if h[A] < h[B]:
        A,B = B,A
    a,b = A,B
    dist = h[a] - h[b]
    for _ in range(dist):
        a = parent[a]
    while a != b:
        a = parent[a]
        b = parent[b]
    common = a


    a,b = A,B
    distance = h[a] + h[b] - 2 * h[common]
    d = distance//2
    for _ in range(d):
        a = parent[a]
    if h[B] < h[A]:
        a = parent[a]
    
    fils = [[] for _ in range(n)]
    to_see = [a]
    seen = [False] * n
    while to_see != []:
        
        u = to_see.pop()
        seen[u] = True
        for v in g[u]:
            if not(seen[v]):
                fils[u].append(v)
                seen[v] = True
                to_see.append(v) 
    
    d1 = [-1] * n
    d2 = [-1] * n 

    def dist_comeback(u):
        if fils[u] == []:
            return 0
        else:
            if d1[u] != -1:
                return d1[u]
            else:
                s = 0
                for v in fils[u]:
                    s += 2 + dist_comeback(v)
                d1[u] = s
                return s 
    
    def dist(u):
        if fils[u] == []:
            return 0
        else:
            if d2[u] != -1:
                return d2[u]
            
            fils[u].sort(key= lambda x:dist_comeback(x) - dist(x))
            s = 0
            for v in fils[u]:
                s += 2 + dist_comeback(v)
            s += dist(fils[u][-1]) - dist_comeback(fils[u][-1]) - 1
            d2[u] = s
            return s

    score = dist(a)
    score += distance//2
    score += distance%2

    p.append(score)

for x in p:
    print(x)


""" 

1
6
2 1
1 2
2 3
3 4
3 5
3 6

"""
