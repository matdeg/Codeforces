t = int(input())
p = []
for _ in range(t):
    n = int(input())
    l = list(map(lambda x : abs(int(x)),input().split()))
    p.append(sum(l))
for x in p:
    print(x)