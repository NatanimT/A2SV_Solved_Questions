n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
sumn = 0
ans = 0

for r in range(n):
    sumn += a[r]
    
    while sumn > s:
        sumn -= a[l]
        l += 1
    
    ans += (r - l + 1)

print(ans)
