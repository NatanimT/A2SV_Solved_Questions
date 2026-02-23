t = int(input())
n = list(map(int, input().split()))
n.sort()
k = 1
for i in n:
    if i >= k:
        k += 1

print(k-1) 
