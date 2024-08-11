t = int(input()) 

color_to_ind = {"C" : 0, "D" : 1, "H" : 2, "S" : 3}



for _ in range(t):
    n = int(input())
    trump = input()
    l = input().split()
    trump_list = []
    color_list = [[] for _ in range(3)]

    def ind(c):
        return color_to_ind[c] - (c >= trump)
    for x in l:
        if x[1] == trump:
            trump_list.append(x)
        else:
            color_list[ind(x[1])].append(x)
    trump_list.sort()
    for i in range(3):
        color_list[i].sort()

    a,b,c,d = len(color_list[0]),len(color_list[1]),len(color_list[2]),len(trump_list)
    a %= 2
    b %= 2
    c %= 2
    d -= a + b + c
    if d >= 0:
        
        for i in range(3):
            while len(color_list[i]) >= 2:
                a = color_list[i].pop()
                b = color_list[i].pop()
                # a > b 
                print(b, end=" ")
                print(a)
        for i in range(3):
            if len(color_list[i]) == 1 and trump_list != []:
                b = color_list[i][0]
                a = trump_list.pop()
                print(b, end = " ")
                print(a) 
        for i in range(len(trump_list)//2):
            print(trump_list[2*i],end = " ")
            print(trump_list[2*i + 1])
    else:
        print("IMPOSSIBLE")
