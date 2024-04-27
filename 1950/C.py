t = int(input())
p = []
for _ in range(t):
    h,m = input().split(":")
    c = "AM"
    if int(h) == 0:
        h = "12"
    else:
        if int(h) >= 12:
            c = "PM"
        if int(h) >= 13:
            h = str(int(h) - 12)
            if int(h) <= 9:
                h = "0" + h 
    
    p.append("{}:{} {}".format(h,m,c))
for x in p:
    print(x)