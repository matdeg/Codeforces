import sys
from io import StringIO 
buffer = StringIO()
input = sys.stdin.readline 
t = int(input().split()[0])

'''
1) transforms the tab in a boolean table where True denotes a change in the values
1 1 2 1 1
becomes
F T T F
if the query is [a,b]
then we search if T is in the table [a,b-1]
'''

def ans(j):
    n = int(input().split()[0])
    tab = list(map(int,input().split()))
    q = int(input().split()[0])
    change = []
    for i in range(n-1):
        if tab[i] != tab[i+1]:
            change.append(i+1)
    for nq in range(q):
        a,b = map(int,input().split())
        # we want to find i in change s.t. a <= c[i] <= b-1
        # we search the first i in change s.t. c[i] >= a
        l,r,m = 0,len(change) - 1,0
        while r-l > 0:
            m = (l+r)//2
            if change[m] >= a:
                r = m
            else:
                l = m+1

        if len(change) > 0 and a <= change[l] < b:
            print("{} {}".format(change[l],change[l]+1))
        else:
            print("-1 -1")
    print("")

for i in range(t):
    ans(i)
