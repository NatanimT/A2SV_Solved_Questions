n, s = map(int, input().split())
a = list(map(int,input().split()))
gap = []
if s == 1:
    print(a[n -1] - a[0] )
  

else:
    for i in range(1,n):
        gap.append(a[i] - a[i -1])
    gap.sort(reverse=True)
    total = a[n -1] - a[0] 

    for i in range(s -1):
        total -= gap[i]
    print(total)
