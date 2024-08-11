t = int(input())
p = []

def power_mod(a,b,q):
    if b == 0:
        return 1
    if b == 1:
        return a%q
    if b%2==0:
        return (power_mod(a, b//2, q)**2)%q
    return (a * (power_mod(a, b//2, q)**2))%q

def my_hash(l):
    s = 0
    prime = 10**9 + 7  
    for i in range(len(l)):
        if l[i] == "1":
            s += power_mod(2,i,prime)
            s %= prime
    return s

for _ in range(t):
    n,m = map(int,input().split())
    tab = [input() for _ in range(n)]
    occ = dict()
    hash_to_str = dict()
    for j in range(m):
        for i in range(n):
            op = []
            for ii in range(n):
                target = ("1" if (ii == i) else "0")
                if target == tab[ii][j]:
                    op.append("0")
                else:
                    op.append("1")
            hsh = my_hash(op)
            if hsh in occ.keys():
                occ[hsh] += 1
            else:
                occ[hsh] = 1
                hash_to_str[hsh] = op
    best = 0 
    best_hash = 0
    for k,v in occ.items():
        if v > best:
            best = v
            best_hash = k
    p.append(best)
    p.append("".join(hash_to_str[best_hash]))

for x in p:
    print(x)