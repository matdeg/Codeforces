t = int(input())
p = []
for _ in range(t):
    n = int(input())
    w = input()
    cmap,cpie,cd = 0,0,0
    for i in range(n-2):
        if w[i:i+3] == "map":
            cmap += 1
        elif w[i:i+3] == "pie":
            cpie += 1
    for i in range(n-4):
        if w[i:i+5] == 'mapie':
            cd += 1
    S = cpie + cmap - cd
    p.append(S)
for x in p:
    print(x)