t = int(input())
for _ in range(t):
    n = 2*int(input())
    for i in range(n):
        for j in range(n):
            if ((i//2) + (j//2))%2 == 0:
                print("#",end="")
            else:
                print(".",end="")
        print()