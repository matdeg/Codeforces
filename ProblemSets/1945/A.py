t = int(input())
p = []
for _ in range(t):
    a,b,c = map(int,input().split())
    # a tents for intro

    tent = a + b//3

    intro_rest = b%3

    if intro_rest > 0 and c < 3-intro_rest:
        p.append(-1)
    else:
        c -= 3-intro_rest
        tent+=1
        tent+= c//3
        if c%3 > 0:
            tent += 1
        p.append(tent)
for x in p:
    print(x)