from collections import Counter
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cntA = Counter(a)
cntB = Counter(b)
ans= 0
for key in cntA:
    if key in cntB:
        ans += cntA[key] * cntB[key]
print(ans)
