'''
gain times k
x loss max
a coins intial

it suffices to show he has a strategy that ensures 
loss loss ... loss win -> +coins

let k = 3
here is the strategy
bet 1
if wins +3

bet 1
if wins +3 - 1 = 2

bet 1
if wins +3 - 2 = 1

bet 2
if wins +6 - 3 = 3

bet 2
if wins +6 - 5 = 1

etc...
x times
if it is "betable" then ok
'''

t = int(input())
p = []
for _ in range(t):
    k,x,a = map(int,input().split())
    b = a
    bet = 1
    for i in range(x):
        b -= bet
        bet = 1 + (a-b)//(k-1)
    b-=bet
    if b >= 0:
        p.append("YES")
    else:
        p.append("NO")
    
for x in p:
    print(x)