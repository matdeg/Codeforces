t = int(input())
for _ in range(t):  
    a,b = map(int,input().split())
    bin_a = [x for x in bin(a)[2:]]
    la = len(bin_a)
    bin_b = ['0'] * la
    bin_word_b = bin(b)[2:]
    lb = len(bin_word_b)
    for i in range(lb):
        bin_b[i + la - lb] = bin_word_b[i]

    ans = []

    swap = [0]


    while swap != []:
        use_one = bin_a.copy()
        pile_down = []
        swap = []
        for i in range(la):
            if bin_a[i] == '1' and bin_b[i] == '0':
                pile_down.append(i)
            if bin_a[i] == "0":
                if bin_b[i] == "1":
                    if pile_down != []:
                        last_i = pile_down[-1]
                        exists1 = False
                        j1 = 0
                        for j in range(i-1,-1,-1):
                            if use_one[j] == "1":
                                exists1 = True
                                j1 = j
                                break
                        if exists1:
                            exists1 = False
                            for j in range(last_i,-1,-1):
                                if use_one[j] == "1" and j != j1:
                                    exists1 = True
                                    use_one[j] = "0"
                                    use_one[j1] = "0"
                                    break
                            if exists1:
                                swap.append(i)
                                swap.append(pile_down.pop())
        S = 0
        for i in swap:
            bin_a[i] = str(1 - int(bin_a[i]))
            S += 2**(la-1-i)
        if S != 0:
            ans.append(S)

    S = 0    
    P = 2**(la-1)
    for i in range(la):
        if bin_a[i] == "1" and bin_b[i] == "0":
            S += P
            bin_a[i] = "0"
        P = P//2
    if S != 0:
        ans.append(S)
    
    ok = True
    for i in range(la):
        if bin_a[i] != bin_b[i]:
            ok = False

    if ok:
        print(len(ans))
        print(a,end = " ")
        for x in ans:
            a = a^x
            print(a,end = " ")
        print()
    else:
        print(-1)




