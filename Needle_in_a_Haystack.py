from collections import Counter
t = int(input())
for _ in range(t):
    s = input().strip()
    t = input().strip()

    countS = Counter(s)
    countT = Counter(t)


    possible = True
    for c in countS:
        if countS[c] > countT[c]:
            possible = False
            break

    if not possible:
        print("Impossible")
        continue


    left = []
    for c in sorted(countT.keys()):
        left.extend([c] * (countT[c] - countS[c]))
    letters = "".join(left)

    res = []
    i = 0  
    for c in letters:
        while i < len(s) and s[i] <= c:
            res.append(s[i])
            i += 1
        res.append(c)
    while i < len(s):
        res.append(s[i])
        i += 1

    print("".join(res))
