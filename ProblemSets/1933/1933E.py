import sys
input = sys.stdin.readline
t = int(input().split()[0])
p_buff = []
for _ in range(t):
    p = []
    n = int(input().split()[0])
    l = list(map(int,input().split()))
    q = int(input().split()[0])
    N = 1
    while N < n:
        N*= 2
    
    tab = [0] * (2*N)
    for i in range(n):
        tab[N + i] = l[i]
    for i in range(N-1,0,-1):
        tab[i] = tab[2*i] + tab[2*i + 1]
    def ask_(l,r,a,b,i):
        if l <= a <= b <= r:
            return tab[i]
        if b < l or a > r:
            return 0
        
        m = (a+b)//2
        return ask_(l,r,a,m,2*i) + ask_(l,r,m+1,b,2*i+1)
    def ask(l,r):
        return ask_(l,r,1,N,1)
    def score(l,r,u):
        ai = ask(l,r)
        return ((ai * (2 * u - ai + 1))//2)
    
    for loop in range(q):
        l,u = map(int,input().split())
        i,j = l,n
        while j-i > 0:
            m = (i+j)//2
            ans = ask(l,m)
            if ans>u+1:
                j = m-1
            elif ans <= u+1:
                i = m+1
        best = -float("inf")
        best_c = 0
        for c in range(max(l,i-2),min(n,i+2)+1):
            sc = score(l,c,u)
            if sc > best:
                best = sc
                best_c = c
        print(best_c, end = " ")
    print()

    