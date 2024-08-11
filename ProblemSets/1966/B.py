t = int(input())
p = []
for _ in range(t):
    n,m = map(int,input().split())
    mat = [input() for _ in range(n)]
    w = [False] * 4
    b = [False] * 4
    for i in range(n):
        if mat[i][0] == "W":
            w[0] = True 
    for i in range(n):
        if mat[i][0] == "B":
            b[0] = True 
    for i in range(n):
        if mat[i][m-1] == "W":
            w[1] = True 
    for i in range(n):
        if mat[i][m-1] == "B":
            b[1] = True 
    for j in range(m):
        if mat[0][j] == "W":
            w[2] = True 
    for j in range(m):
        if mat[0][j] == "B":
            b[2] = True 
    for j in range(m):
        if mat[n-1][j] == "W":
            w[3] = True 
    for j in range(m):
        if mat[n-1][j] == "B":
            b[3] = True 
    if w == [True]*4 or b == [True]*4:
        p.append("YES")
    else:
        p.append("NO")
for x in p:
    print(x)