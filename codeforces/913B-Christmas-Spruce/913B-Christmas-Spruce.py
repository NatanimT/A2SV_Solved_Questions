from collections import Counter
n = int(input())
arr = []
for _ in range(n-1):
    arr.append(int(input()))

m = Counter(arr)

s = 2
for i in arr:
    if s in m:
        m[i] -= 1
    s += 1

for i in m:
    if m[i] < 3:
        print("No")
        exit()
print("Yes")