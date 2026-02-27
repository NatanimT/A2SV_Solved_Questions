t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    s = input().strip()
    white = 0
    for i in range(k):
        if s[i] == 'W':
            white += 1
    ans = white
    
    for r in range(k, n):
        if s[r] =='W':
            white += 1
        if s[r-k] == 'W':
            white -= 1
        ans = min(ans, white)
    print(ans)
        
