t = int(input())
p = []
for _ in range(t):
    n = int(input())
    w = input()
    s = 0
    for c in w:
        if c == "U":
            s += 1
    if s%2==0:
        p.append("NO")
    else:
        p.append("YES")
for x in p:
    print(x)