t = int(input())
p = []
for _ in range(t):
    n = int(input())
    

    number = input()
    tab_number = [0] * (n+1)
    tab_retenue = [0] * (n+1)

    S = 0
    for c in number:
        S += c

    for i in range(n-1,-1 -1):
        s = string(S)
        k = len(s)
        for j in range(k-1,-1,-1):
            tab_number[i + j - (k-1)] += s[j] + r[i + j - (k+1)]
            
        



    
