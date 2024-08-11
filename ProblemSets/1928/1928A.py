t = int(input())
for loop in range(t):
    a,b = map(int,input().split())
    if a%2 == 1 and b%2 == 1:
        print("NO")
    else:
        if a%2 == 1:
            a,b = b,a
        assert(a%2 == 0)
        if b%2 == 1 and 2*b == a:
            print("NO")
        else:
            print("YES")