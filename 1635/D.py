n,p = map(int,input().split())
tab = [set() for _ in range(34)]
l = list(map(int,input().split()))
l.sort()
for x in l:
    lg = len(bin(x)) - 2
    tmp = x
    tmpl = lg
    stop = False 
    found = False 
    while not(stop) and tmpl >= 1:
        if tmp % 4 == 0:
            tmp = tmp // 4
            tmpl -= 2
        elif tmp % 2 == 1:
            tmp = tmp//2
            tmpl -= 1
        else:
            break

        if tmp in tab[tmpl]:
            found = True
            break
    if not(found):
        tab[lg].add(x)

dp = [0 for _ in range(max(10,p+1))]

dp[1] = len(tab[1])
dp[2] = len(tab[2]) + dp[1]
for i in range(3,p+1):
    dp[i] = (dp[i-2] + dp[i-1] + (len(tab[i]) if i < 34 else 0))%(10**9+7)
ans = 0
for i in range(p+1):
    ans += dp[i]
    ans %= (10**9+7)
print(ans)

