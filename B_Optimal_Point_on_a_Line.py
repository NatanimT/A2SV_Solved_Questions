n = int(input())
s = list(map(int,  input().split()))
s.sort()
median_odd =(n +1)// 2 -1
median_even = n // 2 -1
if n % 2 != 0:
    print(s[median_odd])
else:
    print(s[median_even])

