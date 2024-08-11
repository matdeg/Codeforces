t = int(input())
p = []
for _ in range(t):
    n = int(input())
    trace = list(map(int,input().split()))
    alp = dict()
    ans = []
    for i in range(26):
        alp[chr(ord("a") + i)] = 0
    for i in range(n):
        occ = trace[i]
        j = 0
        while alp[chr(ord("a")+ j)] != occ:
            j += 1
        ans.append(chr(ord("a")+ j))
        alp[chr(ord("a")+ j)] += 1
    p.append(ans)
for x in p:
    for c in x:
        print(c,end='')
    print()