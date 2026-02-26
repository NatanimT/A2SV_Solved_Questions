t = int(input())
for _ in range(t):
    s = input()
    working = set()
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            char = s[i]
            while i < len(s) and s[i] == char:
                i += 1
        else:
            working.add(s[i])
            i += 1
    print("".join(sorted(working)))
