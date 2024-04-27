t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    price = n//k
    if price <= n%k:
        print("NO")
    else:
        print("YES")
        print(2)
        print(price, price+1)