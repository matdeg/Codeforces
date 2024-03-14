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
                