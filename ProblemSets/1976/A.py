t = int(input())
p = []

def check_asc_digit(s):
    for i in range(len(s)):
        if not(ord('0') <= ord(s[i]) <= ord('9')):
            return False
    for i in range(len(s)-1):
        if not(ord(s[i]) <= ord(s[i+1])):
            return False
    return True

def check_asc_letter(s):
    for i in range(len(s)):
        if not(ord('a') <= ord(s[i]) <= ord('z')):
            return False
    for i in range(len(s)-1):
        if not(ord(s[i]) <= ord(s[i+1])):
            return False
    return True

for _ in range(t):
    n = int(input())
    w = input()
    
    ok = True

    if ord('0') <= ord(w[0]) <= ord('9'):
        j = 0
        while j < n and ord('0') <= ord(w[j]) <= ord('9'):
            j += 1
        if not(check_asc_digit(w[0:j])):
            ok = False
        i = j
    else:
        i = 0
    s = w[i:n]
    if not(check_asc_letter(s)):
        ok = False
    if ok:
        p.append("YES")
    else:
        p.append("NO")
    


for x in p:
    print(x)