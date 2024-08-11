t = int(input())
import math
p_buff = []
for loop in range(t):
    sol = set()
    
    p,m = map(int,input().split())
    S = 0
    def ad(x):
        if x >= m:
            sol.add(x)
    '''
    if it is first k-th then the range is
    1 2 ... (k-1) k (k-1) ... 2 1 2 ... 
    for exmple with 4 
    1 2 3 4 3 2 1 2 3 4 3 2 1 2 ...
    then the function which takes pos_line,k and gives k is 
    f x : g (x%2k-2)
    where g is 
    g x = k - |x - k|
    so f x = k - |(x%2k-2) - k|

    Finally, the question is 
    find number of k s.t. k - |(p%2k-2) - k| = m
    '''

    '''
     if p%2k-2 is small, is f p = p%2k-2 = m 
     i.e. 
     2(k-1) | p - m so  (p-m)//2 (and m <= k)
     i.e k-1 | (p-m)//2
     if p - m is pair, search for divisors of (p-m)//2 that are greater or equal to m-1 
     '''
    if (p-m)%2==0:
        d = (p-m)//2
        for i in range(1,1 + math.ceil(math.sqrt(d))):
            if d%i == 0:
                if i*i == d:
                    S += 1
                    ad(i+1)
                else:
                    S += 2
                    ad(i+1)
                    ad(d//i + 1)
    '''
    else f p = 2k - p%2k-2 = m
    !!!!! if p = 0 or 1 
    p%2k-2 = 2k - m
    p-2%2k-2 =  - m
    2k-2 | p-2+m 
    '''

    if (p-2+m)%2==0:
        d = (p-2+m)//2
        for i in range(1,1 + math.ceil(math.sqrt(d))):
            if d%i == 0:
                if i*i == d:
                    S += 1
                    ad(i+1)
                else:
                    S += 2
                    ad(i+1)
                    ad(d//i + 1)
    p_buff.append(len(sol))
for x in p_buff:
    print(x)
        