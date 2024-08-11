t = int(input())
p = []

for _ in range(t):
    x = int(input())
    caux = bin(x)[2:]
    c = [caux[i] for i in range(len(caux)-1,-1,-1)]
    c.append("0")
    c.append("0")
    i = 0
    sol = []
    sol = [int(car) for car in c]
    for i in range(len(caux)):
        if sol[i] == 1 and sol[i+1] == 1:
            sol[i] = -1
            sol[i+1] = 0
            sol[i+2] += 1
        if sol[i] == 2:
            sol[i] = 0
            sol[i+1] += 1
    while sol[-1] == 0:
        sol.pop()
    p.append(sol)


for x in p:
    print(len(x))
    print(*x)


"""

1 1 1 1 1 1 1 1 1 1  

-1 0 2 1 1 1 1 1 1 1

-1 0 0 2 1 1 1 1 1 1 

...

-1 0 0 0 0 0 0 0 0 0 1

13 is 
1101
reversed is 
1 0 -1 0 1 0 0 0

1 0 -1 0 1


"""