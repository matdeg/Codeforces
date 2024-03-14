import sys
input = sys.stdin.readline
t = int(input().split()[0])
pbuff = []
def cycle(g,n):
    global has_cycle
    WHITE = 0
    GRAY = 1
    BLACK = 2
        
        
    ENTER = 0
    EXIT = 1
    
    has_cycle = False 
    state = {v: WHITE for v in range(n)}
    
    def parcours(u):
        global has_cycle
        stack = [(ENTER, u)]
        while stack:
            act, v = stack.pop()
            if act == EXIT:
                state[v] = BLACK
            else:
                state[v] = GRAY
                stack.append((EXIT, v))
                for n in g[v]:
                    if state[n] == GRAY:
                        has_cycle = True
                    elif state[n] == WHITE:
                        stack.append((ENTER, n))

    for v in range(n):
        if state[v] == WHITE:
            parcours(v)

    return has_cycle

    





def main():
    for loop in range(t):
        n,k = map(int,input().split())
        g = [set() for _ in range(n)]

        for i in range(k):
            s = list(map(int,input().split()))
            for j in range(1,n-1):
                g[s[j] - 1].add(s[j+1] - 1)
        if cycle(g,n):
            pbuff.append("NO")
        else:
            pbuff.append("YES")
    
main()

for x in pbuff:
    print(x)