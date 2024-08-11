class SegmentTree():
    def __init__(self,tab):
        self.N = 1 
        n = len(tab)
        while self.N < n:
            self.N *= 2
        self.tab = [0] * (2 * self.N)
        for i in range(n):
            self.tab[self.N + i] = tab[i]
        for i in range(self.N-1,0,-1):
            self.tab[i] = self.tab[2*i] + self.tab[2*i + 1]
        
    def sum_(self,a,b,l,r,i):
        if a <= l <= r <= b:
            return self.tab[i]
        if r >= a and l <= b:
            m = (l+r)//2
            return self.sum_(a,b,l,m,2*i) + self.sum_(a,b,m+1,r,2*i+1)
        return 0

    def sum(self,a,b):
        return self.sum_(a,b,0,self.N-1,1)

    def prefix_sum(self, k, interdit):
        return self.sum(0,k) - self.tab[interdit+self.N]

    def first_depass(self, n, interdit):
        i = 0
        j = self.N-1
        while j-i > 0:
            m = (i+j)//2
            s = self.prefix_sum(m,interdit)
            if s < n:
                i = m+1
            else:
                j = m
        return i

t = SegmentTree([1,1,1,1,1])
print(t.prefix_sum(0,1))
print(t.first_depass(1,1))