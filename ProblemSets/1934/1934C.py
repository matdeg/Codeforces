t = int(input())

def query(x,y):
    print("? {} {}".format(x,y))
    res = int(input())
    return res

for _ in range(t):
    n,m = map(int,input().split())
    res1 = query(1,1)
    
    x_left = min(n,1+res1)
    y_left = max(1,res1 - n + 2)

    x_right = max(1,res1 - m + 2)
    y_right = min(m,1+res1)

    res2 = query(x_left,y_left)
    res3 = query(x_right,y_right)

    res4 = query(x_left - res2//2, y_left + res2//2)
    if res4 == 0:
        print("! {} {}".format(x_left - res2//2, y_left + res2//2))
    else:
        print("! {} {}".format(x_right + res3//2, y_right - res3//2))

    