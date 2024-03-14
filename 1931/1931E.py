t = int(input())
pbuff = []
import heapq as hp
def count_z(k):
    cnt = 0
    while k%10 == 0:
        k = k//10
        cnt += 1
    return cnt

def ans(n,m,tab):
    desc = [(-count_z(x),len(str(x))) for x in tab]
    hp.heapify(desc)
    rev_z,l = hp.heappop(desc)
    hp.heappush(desc,((0,l+rev_z)))
    while len(desc) > 1:
        rev_z1,l1 = hp.heappop(desc)
        rev_z2,l2 = hp.heappop(desc)
        hp.heappush(desc,(rev_z2,l1+l2))
        rev_z,l = hp.heappop(desc)
        hp.heappush(desc,((0,l+rev_z)))
    if desc[0][1] >= m + 1:
        pbuff.append("Sasha")
    else:
        pbuff.append("Anna")

for loop in range(t):
    n,m = map(int,input().split())
    tab = list(map(int,input().split()))
    ans(n,m,tab)

for x in pbuff:
    print(x)