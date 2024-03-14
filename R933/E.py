class SegmentTree():
    def __init__(self,tab):
        self.N = 1 
        n = len(tab)
        while self.N < n:
            self.N *= 2
        self.tab = [float("inf")] * (2 * self.N)
        for i in range(n):
            self.tab[self.N + i] = tab[i]
        for i in range(self.N-1,0,-1):
            self.tab[i] = min(self.tab[2*i],self.tab[2*i + 1])
        
    def mini_(self,a,b,l,r,i):
        if a <= l <= r <= b:
            return self.tab[i]
        if r >= a and l <= b:
            m = (l+r)//2
            return min(self.mini_(a,b,l,m,2*i),self.mini_(a,b,m+1,r,2*i+1))
        return float("inf")
    
    def mini(self,a,b):
        return self.mini_(max(a,0),min(b,self.N-1),0,self.N-1,1)

    def update(self,i,x):
        self.tab[self.N + i] = x
        k = i + self.N
        while k != 1:
            k = k//2
            self.tab[k] = min(self.tab[2*k + 1],self.tab[2*k])

import sys
t = int(input().split()[0])
p = []
for _ in range(t):
    n,m,k,d = map(int,input().split())
    mp = [list(map(int,input().split())) for _ in range(n)]
    cost = [0] * n
    for i in range(n):
        dp = [0] * m
        t = SegmentTree(dp)
        t.update(0,1)
        dp[0] = 1
        for j in range(1,min(d+2,m)):
            mini = 2 + mp[i][j]
            t.update(j,mini)
            dp[j] = mini
        for j in range(d+2,m):
            mini_prev = t.mini(j-d-1,j-1)
            mini = mini_prev + mp[i][j] + 1
            t.update(j,mini)
            dp[j] = mini
        cost[i] = dp[-1]
    sum = 0
    best = float("inf")
    for i in range(k):
        sum += cost[i]
    best = min(best,sum)
    for j in range(k,n):
        sum += cost[j] - cost[j-k]
        best = min(best,sum)
    p.append(best)
for x in p:
    print(x)