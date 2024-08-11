t = int(input())
p = []
for _ in range(t):
    w = input()
    n = len(w)
    s = 0
    cum = 0
    for i in range(len(w)):
        if w[i] == "0" and cum != 0:
            s += cum + 1
        if w[i] == "1":
            cum += 1
    p.append(s)
for x in p:
    print(x)