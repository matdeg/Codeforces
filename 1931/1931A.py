t = int(input())

def ans(n):
    a,b,c = 1,1,1
    c = min(26,n-2)
    b = max(min(26,n - 27),1)
    a = max(n - 52,1)
    print(chr(ord("a") + a - 1) +chr(ord("a") + b - 1) +chr(ord("a") + c - 1))

for loop in range(t):
    ans(int(input()))