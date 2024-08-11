'''
a tree is represented by a couple good_ancestor,good_sep
the first is the number of good sets such that there are two dangerous cities 
with a parent link. the other one is the opposite

let's consider the node N(A,g,d)
where g = (g0,g1) and d = (d0,d1)
a good set verifies :
    - if A is dangerous, then
        - either g and d are empty, it counts as +1 for good_sep
        TODO - if g or d is non empty, if both are good_sep, then it becomes goodancestor
          so +(d1.g1 - 1) for good_ancestor 
        - if g or d is non empty and one is good anc, then it is not godo anymore
    - if A is not dangerous, then
        - if g and d are goodsep, then it is good sep
          +g1.d1 for goodsep
        - if g is good ancestor, and d is good, non empty, it's dead.
        - same for d good ancestor, with g good and non empty
        so only remains
        - g good ancestor and d empty, then its ancestor, and the inverse
          g0 + d0 for good incestor

for a leaf, we have the couple (0,2)
then, N(a,g,d) = (g0 + d0 + d1-1 + g1-1, g1.d1 + 1)

in the case of more than two childs,
N(a,k,l,m) = (k0 + l0 + m0 + (k1-1) + (l1-1) + (m1-1), 1 + k1.l1.m1)
ex. with the tree 
        1
      (6,6)

        3
       (2,5)
        
    2       4
   (0,2)   (0,2) 
'''     

import sys
MOD = 998244353
WHITE = 0
GREY = 1
BLACK = 2
input = sys.stdin.readline

def parcours(g,n):
    fils = [[] for _ in range(n)]
    values = [(0,2) for _ in range(n)]
    seen = [False for _ in range(n)]
    pile = [(0,WHITE)]
    while pile != []:
        u,c = pile.pop()
        if not(seen[u]) and c == WHITE:
            seen[u] = True
            pile.append((u,BLACK))
            for v in g[u]:
                if not(seen[v]):
                    pile.append((v,WHITE))
                    fils[u].append(v)
        elif c == BLACK:
            S0 = 0
            S1 = 0
            P1 = 1
            for v in fils[u]:
                v1,v2 = values[v]
                S0 = (S0 + v1)%MOD
                S1 = (S1 + v2 - 1)%MOD
                P1 = (P1 * v2)%MOD
            values[u] = ((S0 + S1)%MOD,(1 + P1)%MOD)
    return (values[0][0] + values[0][1])%MOD
    



t = int(input().split()[0])
p = []
for _ in range(t):
    n = int(input().split()[0])
    g = [[] for i in range(n)]
    for _ in range(n-1):
        a,b =  map(int,input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    p.append(parcours(g,n))
for x in p:
    print(x)
