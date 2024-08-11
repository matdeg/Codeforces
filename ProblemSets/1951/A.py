t = int(input())
p = []
for _ in range(t):
    n = int(input())
    w = input()
    ones = 0
    pos = []
    for i,c in enumerate(w):
        if c == "1":
            ones += 1
            pos.append(i)
    if ones%2 == 1:
        p.append("NO")
    else:
        if ones >= 4 or ones == 0:
            p.append("YES")
        else:
            if pos[0] + 1 == pos[1]:
                p.append("NO")
            else:
                p.append("YES")
for x in p:
    print(x)