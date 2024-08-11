t = int(input())
p_buff = []
p_test = []
for loop in range(t):

    n,b,x = map(int,input().split())
    '''let's make a function that first computes the bonus points
    of an army. we can hope it is increasing then decreasing and do 
    a ternary search'''
    l = list(map(int,input().split()))
    def bonus(g):
        if g == 0:
            return -float("inf")
        ''' returns the bonus when using g groups
            this function is increasing in g'''
        S = 0
        for i in range(n):
            S += (l[i]%g) * (l[i]//g + 1) * (l[i] - l[i]//g - 1)
            S += (g - l[i]%g) * (l[i]//g) * (l[i] - l[i]//g)
        return S//2
    
    def malus(g):
        ''' 
        returns the malus when using g groups
        this function is increasing in g
        '''
        return g-1
    
    def score(g):
        return b * bonus(g) - x * malus(g)
    
    '''
    we want to find g maximising score(g)
    '''

    i = 1
    j = max(l)
    while j-i > 0:
        
        m = (i+j)//2
        if score(m-1) <= score(m) <= score(m+1):
            '''increasing at m'''
            i = m+1
        elif score(m-1) >= score(m) >= score(m+1):
            '''decreasing at m'''
            j = m
        else:
            i = m
            j = m
    p_test.append(score(i))
for x in p_test:
    print(x)
