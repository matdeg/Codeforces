t = int(input())
p = []
for _ in range(t):
    n = int(input())
    w = input()
    i = 0
    j = n-1
    while i < n and w[i] == "W":
        i+=1
    while j >= 0 and w[j] == "W":
        j -= 1
    if j == -1:
        p.append(0)
    else:
        p.append(j-i+1)
for x in p:
    print(x)