t = 100000000
q = 998244353
fact = [1]
import random as rd
for i in range(1,2000000):
    fact.append((fact[-1] * i)%q)

def pow_mod(a, b):
    """Compute (a pow b) % q
    :param int a b: non negative
    :param int q: positive
    :complexity: O(log b)
    """
    assert a >= 0 and b >= 0 and q >= 1
    p = 0 # only for documentation
    p2 = 1 # 2 ** p
    ap2 = a % q # a ** (2 ** p)
    result = 1
    while b > 0:
        if p2 & b > 0: # b's binary decomposition contains 2 ** p
            b -= p2
            result = (result * ap2) % q
        p += 1
        p2 *= 2
        ap2 = (ap2 * ap2) % q
    return result

def inv(a):
    return pow_mod(a,q-2)

def cnk(k,n):
    res = fact[n]
    res = (res * inv(fact[k]))%q
    return (res * inv(fact[n-k]))%q

for loop in range(t):
    if loop == 0:
        c1,c2,c3,c4 = 900000,900000,900000,900000
    else:
        
        c1,c3,c4 = rd.randint(0,1000000),rd.randint(0,1000000),rd.randint(0,1000000)
        c2 = rd.randint(max(0,c1-1),c1+1)
        print(c1,c2,c3,c4)
    if abs(c1 - c2) > 1:
        print(0)
    elif c1 + c2 == 0:
        if c3 == 0 or c4 == 0:
            print(1)
        else:
            print(0)
    else:
        r = 0      
        if c1 <= c2:
            """ 
            [c3] c2 [c4] c1 [c3] c2 [c4]
            """
            r += (cnk(c3,c1+c3) * cnk(c4,c2+c4-1)) % q

        if c1 >= c2:
            """ 
            [c4] c1 [c3] c2 [c4] c1 [c3]
            """
            r += (cnk(c3,c2+c3) * cnk(c4,c1+c4-1)) % q
        print(r%q)
