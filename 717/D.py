'''
Let A be the matrix Aij = (P(i^j))
So, if x = 2, then 

A = 
( 0.5   0.25    0.25    0   ) 
( 0.25  0.5     0       0.25)
( 0.25  0       0.5     0.25)
( 0     0.25    0.25    0.5 )

'''

n,x = map(int,input().split())

N = 1
while N <= x:
    N *= 2

P_aux = list(map(float,input().split()))
P = [0] * N
for i in range(x+1):
    P[i] = P_aux[i]
A = [[P[i ^ j] for j in range(N)] for i in range(N)]

def produit(A,B):
    C = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            S = 0
            for k in range(N):
                S += A[i][k] * B[k][j]
            C[i][j] = S
    return C

def produit_ext(A,X):
    Y = [0 for _ in range(N)]
    for i in range(N):
        S = 0
        for k in range(N):
            S += A[i][k] * X[k]
        Y[i] = S
    return Y

def puissance(A,n):
    if n == 1:
        return A
    
    elif n%2 == 0:
        return puissance(produit(A,A),n//2)
    else:
        return produit(A,puissance(produit(A,A),n//2))
    
print(1 - produit_ext(puissance(A,n-1),P)[0])