t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ls = sorted(l)
    mex = 0
    for i in range(n):
        if ls[i] == mex:
            mex += 1
    sol = []
    possible = True
    if mex == 0:
        sol.append((0,0))
        sol.append((1,n-1))
    else:
        i = 0
        j = 0
        while j < n:
            s = set()
            cur_mex = 0
            while j < n and cur_mex != mex:
                s.add(l[j])
                while cur_mex in s:
                    cur_mex += 1
                j += 1
            if cur_mex == mex:
                sol.append((i,j-1))
            i = j
    if len(sol) == 1:
        possible = False
    if possible:
        print(len(sol))
        for i in range(len(sol)):
            if i == len(sol) -1:
                a,b = sol[i]
                print("{} {}".format(a+1,n))
            else:
                a,b = sol[i]
                print("{} {}".format(a+1,b+1))
    else:
        print(-1)
    



'''
5
2
0 0
5
0 1 2 3 4
8
0 1 7 1 0 1 0 3
3
2 2 2
4
0 1 2 0


 t   017 1 01 03
Mex   2  0  2  1

'''