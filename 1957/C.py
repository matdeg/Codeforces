t = int(input())
p = []
dp = [0] * (3 * 10**5 + 1)
MOD = 10**9 + 7

dp[0] = 1
dp[1] = 1
for i in range(2,len(dp)):
    dp[i] = dp[i-1] + 2 * (i-1) * dp[i-2]
    dp[i] %= MOD

for _ in range(t):
    n,k = map(int,input().split())
    for _ in range(k):
        a,b = map(int,input().split())
        if a == b:
            n -= 1
        else:
            n -= 2
    p.append(dp[n])
for x in p:
    print(x)