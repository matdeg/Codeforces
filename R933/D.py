t = int(input())
for _ in range(t):
    n,m,x = map(int,input().split())
    t = [0] * n
    t[x-1] = 1
    new_t = [0] * n
    for _ in range(m):
        r,d = input().split()
        r = int(r)
        new_t = [0] * n
        for i in range(n):
            if d == "0":
                new_t[i] = t[(i-r)%n]
            elif d == "1":
                new_t[i] = t[(i+r)%n]
            else:
                new_t[i] = max(t[(i-r)%n],t[(i+r)%n])
        for i in range(n):
            t[i] = new_t[i]
    print(sum(t))
    for i in range(n):
        if t[i] == 1:
            print(i+1,end=" ")
    print()