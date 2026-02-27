t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    ans = []
    for _ in range(n):
        l,r,real = map(int, input().split())
        ans.append((l,r, real))
    ans.sort()
    for l,r, real in ans:
        if l <= k <= real:
            k = max(k, real)
    print(k)
            
     
