t = int(input())

def ans(n,tab):
    S = sum(tab)
    possible = True
    target = S//n
    bank = 0
    for i in range(n):
        if tab[i] > target:
            bank += tab[i] - target
        if tab[i] < target:
            if bank < target-tab[i]:
                possible = False
            else:
                bank -= target - tab[i]
    if possible:
        print("YES")
    else:
        print("NO")

for loop in range(t):
    n = int(input())
    tab = list(map(int,input().split()))
    ans(n,tab)