import math 
t = int(input())
coin = [1,3,6,10,15]
dp = [0 for loop in range(301)]
p = [] 
dp[1] = 1
for i in range(2,99):
    best = float("inf")
    of = -1
    for ic in range(5):
        if coin[ic] <= i:
            if 1 + dp[i-coin[ic]] < best:
                of = coin[ic]
            best = min(best,1 + dp[i-coin[ic]])

    print("antecedant de {} : {}".format(i,of))
    dp[i] = best

for _ in range(t):
    n = int(input())
    if n <= 300:
        p.append(dp[n])
    else:
        p.append((n-286)//15 + dp[n - 15*((n-286)//15)])

for x in p:
    print(x) 
