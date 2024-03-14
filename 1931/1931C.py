t = int(input())

def ans(n,tab):
    i = 0
    j = n-1
    while i <= n-2 and tab[i+1] == tab[i]:
        i += 1
    if i < n-1:
        while tab[j-1] == tab[j]:
            j -= 1
    if tab[0] == tab[n-1]:
        return max(j-i-1,0)
    else:
        best = max(i + 1,n-j)
        return n - best

for loop in range(t):
    print(ans(int(input()),list(map(int,input().split()))))
