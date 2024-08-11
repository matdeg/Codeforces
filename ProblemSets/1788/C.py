t = int(input())
for _ in range(t):
    n = int(input())
    if n%2==0:
        print("NO")
    else:
        k = n//2
        print("YES")
        for i in range(k):
            print("{} {}".format(i+1,2*n - k+i))
            print("{} {}".format(n-i,n+k-i))
        print("{} {}".format(k+1,2*n))


