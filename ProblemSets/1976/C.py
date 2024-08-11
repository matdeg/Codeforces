
def first_depass(a,k,interdit):
    i = 

import sys
input = sys.stdin.readline


t = int(input().split()[0])
p = []


for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a_pris = []
    b_pris = []
    acc_score = 0
    best_acc_score = []
    for i in range(0,n+m+1):
        if a[i] > b[i]:
            a_pris.append(1)
            b_pris.append(0)
            acc_score += a[i]
        else:
            a_pris.append(0)
            b_pris.append(1)
            acc_score += b[i]
        best_acc_score.append(acc_score)
    
    ta = SegmentTree(a_pris)
    tb = SegmentTree(b_pris)

    suffix_b = [0] * (n+m+2)
    suffix_a = [0] * (n+m+2)
    for i in range(n+m,-1,-1):
        suffix_a[i] = suffix_a[i+1] + a[i]
        suffix_b[i] = suffix_b[i+1] + b[i]

    sol = []
    if n > 0 and m > 0:
        for interdit in range(n+m+1):
            fa = ta.first_depass(n,interdit)
            fb = tb.first_depass(m,interdit)
            if fa <= fb:
                stop = fa
                score = best_acc_score[stop] + suffix_b[stop+1]
                if interdit <= stop:
                    score -= (max(a[interdit],b[interdit]))
                else:
                    score -= b[interdit]
                sol.append(score)
            else:
                stop = fb
                score = best_acc_score[stop] + suffix_a[stop+1]
                if interdit <= stop:
                    score -= (max(a[interdit],b[interdit]))
                else:
                    score -= a[interdit]
                sol.append(score)
    if n == 0:
        for interdit in range(n+m+1):
            score = suffix_b[0] - b[interdit]
            sol.append(score)
    if m == 0:
        for interdit in range(n+m+1):
            score = suffix_a[0] - a[interdit]
            sol.append(score)
    print(*sol)
 