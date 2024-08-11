t = int(input())
q = 998244353
fact = [1]
for i in range(1,4000002):
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
    c1,c2,c3,c4 = map(int,input().split())

    if abs(c1 - c2) > 1:
        print(0)
    elif c1 + c2 == 0:
        if c3 == 0 or c4 == 0:
            print(1)
        else:
            print(0)
    else:
        if c1 == c2:
            """ 
            case x0:
            [c4] c1 [c3] c2 [c4] 
            """
            """ 
            case x1:
            [c3] c2 [c4] c1 [c3] 
            """

            x0 = (cnk(c3,c1+c3-1) * cnk(c4,c1+c4)) % q
            
            x1 = (cnk(c3,c1+c3) * cnk(c4,c1+c4-1)) % q
            print((x0 + x1)%q)
        if c1 < c2:
            """ 
            [c3] c2 [c4] c1 [c3] c2 [c4]
            """
            print((cnk(c3,c2+c3-1) * cnk(c4,c2+c4-1)) % q)

        if c1 > c2:
            """ 
            [c4] c1 [c3] c2 [c4] c1 [c3]
            """
            print((cnk(c3,c1+c3-1) * cnk(c4,c1+c4-1)) % q)

        

