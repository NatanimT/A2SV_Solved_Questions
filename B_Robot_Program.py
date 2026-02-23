t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = []
    curr = 0

    for ch in s:
        if ch == 'L':
            curr -= 1
        else:
            curr += 1
        pref.append(curr)
    f_hit = -1
    for i in range(n):
        if x + pref[i] == 0:
            f_hit = i + 1  
            break
    
    if f_hit == -1 or f_hit > k:
        print(0)
        continue

    len = -1
    for i in range(n):
        if pref[i] == 0:
            len = i + 1
            break

    if len == -1:
        print(1)
        continue
    r = k - f_hit
    addl = r // len
    
    print(1 + addl)
