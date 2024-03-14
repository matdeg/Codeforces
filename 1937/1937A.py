t = int(input())
p = []
for _ in range(t):
    a = int(input())
    n = 1
    while n <= a:
        n *= 2
    n = n//2
    p.append(n)
for x in p:
    print(x)