from math import sqrt

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

def decomp_naif(x):
    p = premiers(int(sqrt(x)) + 1)
    tmp = x
    decomp = []
    finished = False
    while not(finished):
        finished = True
        for pi in p:
            if tmp%pi == 0:
                decomp.append(pi)
                tmp = tmp//pi
                finished = False
    return decomp

def power_mod(a,b,q):
    if b == 1:
        return a%q
    if b%2==0:
        return (power_mod(a, b//2, q)**2)%q
    return (a * (power_mod(a, b//2, q)**2))%q

def inv(x,q):
    #return inverse of x modulo q if q is prime
    return power_mod(x,q-2,q)

                