from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)
l = 0
distinct = 0
ans = 0

for r in range(n):
    if count[a[r]] == 0:
        distinct += 1
    count[a[r]] += 1

    while distinct > k:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            distinct -= 1
        l += 1

    ans += (r - l + 1)

print(ans)
