
class Tas():
    def __init__(self):
        self.taille = 5
        self.present = 0
        self.tab = [-1]*5
    
    def max(self):
        return self.tab[0]

    def insert(self,x):
        if self.taille == self.present:
            new_tab = [-1] * (2 * self.taille)
            for i in range(self.taille):
                new_tab[i] = self.tab[i]
            self.tab = new_tab
            self.taille *= 2
        
        self.tab[self.present] = x
        i = self.present
        while i > 0 and self.tab[i] > self.tab[(i-1)//2]:
            self.tab[i],self.tab[(i-1)//2] = self.tab[(i-1)//2],self.tab[i]
            i = (i-1)//2
        self.present += 1
        
    def remove_max(self):
        self.tab[0] = self.tab[self.present-1]
        self.tab[self.present-1] = -1
        self.present -= 1
        i = 0
        while self.tab[i] < self.tab[2*i+1] or self.tab[i] < self.tab[2*i+2]:
            if self.tab[i] < self.tab[2*i+1]:
                j = 2*i+1
            else:
                j = 2*i+2
            self.tab[i],self.tab[j] = self.tab[j],self.tab[i]
            i = j
            
         

p=[]

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ab = [(a[i],b[i]) for i in range(n)]
    ab.sort(key=lambda x : (-x[1],-x[0]))
    i=k
    a = [x[0] for x in ab]
    b = [x[1] for x in ab]
    tas = Tas()
    profit = 0
    for j in range(k):
        tas.insert(a[j])
        profit -= a[j]
    
    for j in range(k,n):
        if b[j] > a[j]:
            profit += b[j] - a[j]
    
    max_profit = profit
    for i in range(k+1,n):
        if b[i-1] > a[i-1]:
            profit -= (b[i-1] - a[i-1])
        new_b = a[i-1] 
        prev_b = tas.max()
        if new_b < prev_b:
            tas.remove_max()
            tas.insert(new_b)
            profit -= new_b
            profit += prev_b
        max_profit = max(max_profit,profit)
    p.append(max_profit)
for x in p:
    print(max(0,x))
