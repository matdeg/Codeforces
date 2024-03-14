t = int(input())
p = []
for _ in range(t):
    a,b,l = map(int,input().split())
    S = 0
    k_set = set()
    pa = 0
    pb = 0
    a_cum = 1
    b_cum = 1
    while l%(a_cum) == 0:
        while l%(a_cum * b_cum) == 0:
            k = l//(a_cum * b_cum)
            k_set.add(k)
            b_cum *= b
        b_cum = 1
        a_cum *= a
    p.append(len(k_set))
for x in p:
    print(x)