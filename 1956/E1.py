import sys
input = sys.stdin.readline

def main():
    t = int(input().split()[0])

    for _ in range(t):
        n = int(input().split()[0])
        l = list(map(int,input().split()))
        change = True
        alive = set()
        for i in range(n):
            if l[i] > 0:
                alive.add(i)
        while change:
            change = False
            to_rem = []
            for i in alive:
                if l[(i+1)%n] > 0 and l[i] > 0:
                    change = True
                    l[(i+1)%n] = max(0,l[(i+1)%n] - l[i])
                    if l[(i+1)%n] == 0:
                        to_rem.append((i+1)%n)
            for i in to_rem:
                alive.remove(i)
        print(len(alive))
        p = []
        for x in alive:
            p.append(x+1)
        print(*p)

main()