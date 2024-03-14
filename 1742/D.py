from math import gcd

'''
just notice that values in the list are between 1 and 1000
so a lot of these appears multiple times, we just care of last occurence, since
it maximizes the index.

We create a (small) dictionnary d, s.t. d[x] = last occurence of x
then we search among all x,y in the keys of d verifying x^y=1, the maximum of
d[x] + d[y]

there are at most 10⁶ couples, so that's fast enough'''

t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    d = dict()
    for i in range(n):
        d[l[i]] = i
    maxi = -3
    for x in d.keys():
        for y in d.keys():
            if gcd(x,y) == 1:
                maxi = max(maxi,d[x] + d[y])
    p.append(maxi+2)
for x in p:
    print(x)


