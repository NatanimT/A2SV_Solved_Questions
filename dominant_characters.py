t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
        
    answer = float('inf')
        
    for i in range(n):
        for length in [2, 3, 4, 7]:
            if i + length <= n:
                sub = s[i:i+length]
                if sub.count('a') > sub.count('b') and sub.count('a') > sub.count('c'):
                    answer = min(answer, length)
        
    print(answer if answer != float('inf') else -1)
