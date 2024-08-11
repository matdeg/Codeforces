""" 
3 op 
1 5 15 15 15

gluttony gives 1 5 5 5 5
but we can get 1 1 1 1 15

dp[i][j][k] best for [1..i] with j moves such that l[i] became l[i-k]

with i <= 3.10⁵ and 0 <= k <= j <= 10

"""

t = int(input())
p = []
for _ in range(t):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    dp = [[[0] * (k+1) for _ in range(k+1)] for _ in range(n)]
    dp[0][0][0] = l[0]
    for i in range(1,n):
        dp[i][0][0] = dp[i-1][0][0] + l[i]
    
    for i in range(1,k+1):
        dp[i][i][m] = l[i-m] * (i+1)


    for i in range(1,n):
        for j in range(k+1):
            for m in range(min(j+1,i+1)):

                dp[i][j][m] = "???"
            