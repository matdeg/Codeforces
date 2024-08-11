t = int(input())
p = []

def reverse(w):
    n = len(w)
    s = ''
    for i in range(n-1,-1,-1):
        s += w[i]
    return s

for _ in range(t):
    k = int(input())
    w = input()
    if w[0] < w[-1]:
        p.append(w)
    elif w[0] > w[-1]:
        p.append(reverse(w) + w)
    else:
        rw = reverse(w)
        if w <= rw:
            p.append(w)
        else:
            p.append(rw + w)
    
for x in p:
    print(x)