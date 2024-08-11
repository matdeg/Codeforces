t = int(input())
for _ in range(t):
    n = int(input())
    tab = [input() for _ in range(2)]

    dp = [0,0]
    dp_sol = [[],[]]

    dp = [1,1]
    dp_sol = [[tab[0][0]],[tab[0][0],tab[1][0]]]
    for i in range(1,n):
        s1,s2 = dp_sol
        dp_sol[0].append(tab[0][i])
        if dp_sol[0] == dp_sol[1]:
            dp_sol[1].append(tab[1][i])
            dp[1] = 1 + dp[1]
        elif dp_sol[0] < dp_sol[1]:
            dp_sol[1] = dp_sol[0].copy()
            dp_sol[1].append(tab[1][i])
            dp[1] = dp[0]
        else:
            dp_sol[1].append(tab[1][i])

    for x in dp_sol[1]:
        print(x,end = "")
    print()
    print(dp[1])

