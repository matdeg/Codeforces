def query(a,b,c,d):
    print("? {} {} {} {}".format(a,b,c,d))
    res = input()
    return res

def query_same(a,b):
    return query(a,a,b,b)

t = int(input())
for _ in range(t):
    n = int(input())

    best1 = 0
    for i in range(1,n):
        res1 = query_same(best1,i)
        if res1 == "<":
            best1 = i

    S = {0}
    best2 = 0
    for i in range(1,n):
        res2 = query(best1,best2,best1,i)
        if res2 == "<":
            best2 = i
            S = {i}
        if res2 == "=":
            S.add(i)
        
    best3 = best1
    for i in S:
        res2 = query_same(best3,i)
        if res2 == ">":
            best3 = i
    
    print("! {} {}".format(best1,best3))
    
    
    
    

'''
we know x|x = x so we can compare 2 elements by comparing x|x and y|y
so we can find the max element with (n-1) queries (step 1), let's call it n

then we want to find the complement (bitwise) of n.

First we search all i such that pi|n is maximal 
this can be done with n-1 comparisons too

then, among all of them, we search the minimum.

'''



