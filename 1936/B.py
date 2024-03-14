import sys
input = sys.stdin.readline

class SegmentTree():
    def __init__(self,tab):
        self.N = 1 
        n = len(tab)
        while self.N < n:
            self.N *= 2
        self.tab = [0] * (2 * self.N)
        for i in range(n):
            self.tab[self.N + i] = tab[i]
        for i in range(self.N-1,0,-1):
            self.tab[i] = self.tab[2*i] + self.tab[2*i + 1]
        
    def sum_(self,a,b,l,r,i):
        if a <= l <= r <= b:
            return self.tab[i]
        if r >= a and l <= b:
            m = (l+r)//2
            return self.sum_(a,b,l,m,2*i) + self.sum_(a,b,m+1,r,2*i+1)
        return 0
    def sum(self,a,b):
        a = max(0,a)
        b = min(self.N-1,b)
        return self.sum_(a,b,0,self.N-1,1)

def test():
    n = int(input().split()[0])
    seq = input().split()[0]
    left = []
    right = []
    for i in range(n):
        if seq[i] == ">":
            right.append(i)
        else:
            left.append(i)

    lenR = len(right)
    lenL = len(left)
    
    tleft = SegmentTree(left)
    tright = SegmentTree(right)
    r_l_side = 0
    l_r_side = lenL
    position_left = -1
    position_right = 0
    sortie = 0 #i.e. left 
    for i in range(n):
        """ print("case n°{}".format(i)) """
        #update lr and rl
        if seq[i] == "<":
            l_r_side -= 1
        #update position in left 
        if l_r_side > 0 and left[position_left + 1] == i:
            position_left += 1
        #compute TTL (time to leave)
        #first compute where we leave
        
        if sortie == 0: 
            if seq[i] == ">":
                if l_r_side <= r_l_side:
                    sortie = 1
            else:
                if r_l_side > l_r_side:
                    sortie = 1
        TTL = n-i if sortie else i+1

        #compute the number of inversion done at left and right
        inv_left = 0
        inv_right = 0
        if r_l_side < l_r_side:
            inv_left = r_l_side
            inv_right = inv_left + (1 if seq[i] == ">" else 0)
        elif l_r_side < r_l_side:
            inv_right = l_r_side
            inv_left = inv_right + (1 if seq[i] == "<" else 0)
        else:
            inv_right = l_r_side
            inv_left = r_l_side

        route_left = -inv_right * i + tleft.sum(position_left+1,position_left+inv_right)
        route_right = inv_left * i - tright.sum(position_right-inv_left,position_right-1)

        """ print("position right : {}".format(position_right))
        print("position left  : {}".format(position_left))
        print("passes on left : {}".format(inv_left))
        print("passes on right: {}".format(inv_right))
    
        print("route left : {}".format(route_left))
        print("route right: {}".format(route_right)) """

        len_route = route_right + route_left
        #update position in right
        if r_l_side < lenR and right[position_right] == i:
            position_right += 1

        #update lr and rl
        if seq[i] == ">":
            r_l_side += 1

        sys.stdout.write(str(len_route * 2 + TTL))
        sys.stdout.write(" ")
    sys.stdout.write("\n")

t = int(input().split()[0])
for _ in range(t):
    test()

'''
>  <  >  <  <  <  >  <  <  >   >
0  1  2  3  4  5  6  7  8  9  10

let's say we don't consider distance to struggle but struggle indices
then the struggles are fixed

{0,2,6,9,10} on right
{1,3,4,5,7,8} on left

then the output for i is 
first we compute where we'll leave in O(1), considering the number of struggles at left and right
then we get the TimeToLeave in O(1)
we compute in O(1) the number of pass we do on left and right
for the case of left, let's say we do P passes.
then we consider the P maximal struggles in Left that are smaller than i and for each of them (x)
we add (i-x) i.e. P.i - sum(x) so we only need to compute the sum of these elements
(same on right side with sum(x) - P.i)

we can compute sum(x) by giving the indexes of wanted elements in the set Left/Right
for example, for i = 5, we want the sum of 0 and 2, i.e. indexes 0 and 1
we would like to find these in O(1)

we maintain a position in left and right to compute the sum, we want it as

        0 1  2  3  4  5  6  7  8  9  10
left   -1 0  0  1  2  3  3  4  5  5   5
right   0 1  1  2  2  2  2  2  2  2   3
'''