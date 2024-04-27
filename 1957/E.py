from math import sqrt

MOD = 10**9 + 7
p = []
def crible(n):
    t = [True] * (n+1)
    t[0] = False
    t[1] = False
    for i in range(2,n+1):
        for ii in range(i * i, n+1,i):
            t[ii] = False
    return t

def premiers(n):
    t = crible(n)
    s = []
    for x in range(n+1):
        if t[x]:
            s.append(x)
    return s

primes = premiers(10**6 + 2)

def solve(n):
    i = 0
    s = 0
    if n >= 1:
        s += 1
    if n >= 4:
        s += 2
    while i < len(primes) and primes[i] <= n:
        s += primes[i] - 1
        s %= MOD
        i += 1
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    p.append(solve(n))
for x in p:
    print(x)
    