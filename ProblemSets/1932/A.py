t = int(input())
p = []
global i 
i = 0 
for _ in range(t):
    n = int(input())
    w = input()
    i = 0
    s = 0
    def possible():
        global i
        if i == n-2:
            if w[i+1] != "*":
                return i+1
            return -1
        elif i <= n-3:
            if w[i+1] != "*":
                return i+1
            elif w[i+2] != "*":
                return i+2
            return -1
        return -1
    while i != -1:
        i = possible()
        if i != -1 and w[i] == "@":
            s += 1
    p.append(s)

for x in p:
    print(x)