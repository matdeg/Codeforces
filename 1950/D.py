def is_bin(n):
    w = str(n)
    for c in w:
        if c != "0" and c != '1':
            return False
    return True

liste_bin = []
for x in range(2,100001):
    if is_bin(x):
        liste_bin.append(x)

def is_prod(n):
    if is_bin(n):
        return True
    else:
        for x in liste_bin:
            if n%x == 0:
                m = n//x
                return is_prod(m)
        return False

t = int(input())
for _ in range(t):
    n = int(input())
    if is_prod(n):
        print("YES")
    else:
        print("NO")