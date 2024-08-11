t = int(input())
p = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    occ = [0] * n
    for x in a:
        occ[x] += 1

    l0 = []
    l1 = []
    for i in range(n):
        if occ[i] == 0:
            l0.append(i)
        elif occ[i] == 1:
            l1.append(i)
    
    mex = n
    if len(l0) > 0:
        mex = min(l0[0],mex)
    if len(l1) > 1:
        mex = min(mex,l1[1])
    
    p.append(mex)
for x in p:
    print(x)
    


''' 
0123456
XXXXXX
XX XXX
    
'''


''' 
0001 gives 

XX
X
X

'''