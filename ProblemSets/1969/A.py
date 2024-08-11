t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    cycle = False
    for i in range(n):
        if l[l[i] - 1] == i+1:
            cycle = True
    if cycle:
        print(2)
    else:
        print(3)