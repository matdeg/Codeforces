import sys
class SegmentTree():
    def __init__(self,tab):
        self.N = 1 
        n = len(tab)
        while self.N < n:
            self.N *= 2
        self.tab = [(-float("inf"),-float("inf"))] * (2 * self.N)
        self.take = [(float("inf"),float("inf"))] * (2 * self.N)
        for i in range(n):
            self.tab[self.N + i] = (tab[i],i)
            self.take[self.N + i] = (1,tab[i])
        for i in range(self.N-1,0,-1):
            self.tab[i] = max(self.tab[2*i],self.tab[2*i + 1])
            self.take[i] = min(self.take[2*i],self.take[2*i + 1])
        
    def maxi(self):
        return self.tab[1]

    def mini(self):
        return self.take[1]

    def die(self,i):
        self.tab[self.N + i] = (-float("inf"),-float("inf"))
        k = i + self.N
        while k != 1:
            k = k//2
            if self.tab[k] == max(self.tab[2*k + 1],self.tab[2*k]):
                change = False 
            else:
                self.tab[k] = max(self.tab[2*k + 1],self.tab[2*k])

    def do_take(self,i):
        a,b = self.take[self.N + i]
        self.take[self.N + i] = (0,b)
        k = i + self.N
        while k != 1:
            k = k//2
            if self.take[k] == min(self.take[2*k + 1],self.take[2*k]):
                change = False 
            else:
                self.take[k] = min(self.take[2*k + 1],self.take[2*k])

    def untake(self,i):
        a,b = self.take[self.N + i]
        self.take[self.N + i] = (1,b)
        k = i + self.N
        change = True
        while change and k != 1:
            k = k//2
            if self.take[k] == min(self.take[2*k + 1],self.take[2*k]):
                change = False 
            else:
                self.take[k] = min(self.take[2*k + 1],self.take[2*k])

    def taken(self,i):
        return self.take[self.N + i][0] == 0

input = sys.stdin.readline
def main():
    t = int(input().split()[0])
    for _ in range(t):
        n = int(input().split()[0])
        v = list(map(int,input().split()))
        expir = list(map(int,input().split()))
        tr = SegmentTree(v)
        maxi,i_max = tr.maxi()
        tr.do_take(i_max)
        tr.die(i_max)
        score = maxi * 1
        best_score = score
        best_k = 1
        for k in range((n-1)//2):
            tr.die(expir[k] - 1)
            if tr.taken(expir[k] - 1):
                tr.untake(expir[k]-1)
                maxi,i_max = tr.maxi()
                tr.do_take(i_max)
                tr.die(i_max)
            maxi,i_max = tr.maxi()
            tr.do_take(i_max)
            tr.die(i_max)
            min_mush = tr.mini()[1]
            score = (k+2) * min_mush
            if score > best_score:
                best_k = k+2
                best_score = score
            if best_score >= ((n+1)//2) * min_mush:
                break
        sys.stdout.write(str(best_score) + " " + str(best_k) + "\n")

main()