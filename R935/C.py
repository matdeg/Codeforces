t = int(input())
p = []
for _ in range(t):
    n = int(input())
    w = input()
    l = []
    rs = 0
    for x in w:
        rs += int(x)
    rl = 0

    l.append((rl,0,rs,n))
    

    for i in range(n):
        if int(w[i]) == 0:
            rl += 1
        else:
            rs -= 1
        l.append((rl,i+1,rs,n-i-1))
    satisfait = [0 if l[i][0] >= (l[i][1]+1)//2 and l[i][2] >= (l[i][3]+1)//2 else 1 for i in range(n+1)]

    to_sort = [(satisfait[i],abs(n/2 - i),i) for i in range(n+1)]
    to_sort.sort()
    p.append(to_sort[0][2])
for x in p:
    print(x)