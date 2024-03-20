t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    l = list(map(int,input().split()))
    moves = input()
    removed = []
    left = 0
    right = n-1
    for c in moves:
        if c == "L":
            removed.append(left)
            left += 1
        else:
            removed.append(right)
            right -= 1
    p = 1
    pr = []
    for i in range(n):
        p *= l[removed.pop()]
        p %= m
        pr.append(p)
    for i in range(n):
        print(pr.pop(), end = " ")
    print()