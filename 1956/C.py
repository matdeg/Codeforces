t = int(input())


for _ in range(t):
    n = int(input())
    line_str = "1"
    for k in range(2,n+1):
        line_str += " " + str(k)

    s = 0
    cpt = 2*n
    for i in range(1,n+1):
        s += i * (2 * i - 1)
    
    print(s,cpt)

    def p(mode,k):
        print(str(mode) + " " + str(k) + " " + line_str)

    for i in range(1,n+1):
        p(1,n+1-i)
        p(2,n+1-i)
    
    