import sys
input = sys.stdin.readline

p = []

from collections import deque
def main():
    t = int(input().split()[0])
    for _ in range(t):
        n,m = map(int,input().split())
        tab = [list(map(int,input().split())) for _ in range(n)]
        def voisins(i,j):
            vois = []
            if j<m-1 and tab[(i+1)%n][j+1] == 0:
                vois.append(((i+1)%n,j+1))
            if tab[(i+1)%n][j] == 0 and tab[(i+2)%n][j] == 0:
                vois.append(((i+2)%n,j))
            return vois
        file = deque()
        file.append((0,0,0))
        seen = [[-1] * m for i in range(n)]
        seen[0][0] = 0
        while not(len(file) == 0):
            i,j,deep = file.popleft()
            for ii,jj in voisins(i,j):
                if seen[ii][jj] == -1:
                    seen[ii][jj] = deep + 1
                    file.append((ii,jj,deep + 1))
        ans = -1
        for i in range(n):
            if seen[i][m-1] != -1:
                end = (seen[i][m-1]-1)%n
                reach = min(abs(end-i),n-abs(end-i))
                if ans != -1:
                    ans = min(ans,seen[i][m-1] + reach)
                else:
                    ans = seen[i][m-1] + reach
        p.append(ans)
    for x in p:
        print(x)


main()