import heapq
import sys
ans = []
heap = []
heapq.heapify(heap)
n = int(input())
for _ in range(n):
    s = input()
    if s[0] == "i":
        opr = s.split(" ")
        heapq.heappush(heap,int(opr[1]))
    elif s[0] == "r":
        if heap:
            heapq.heappop(heap)
        else:
            ans.append('insert 1')
    else:
        x = s.split(" ")
        while heap and heap[0] < int(x[1]):
            heapq.heappop(heap)
            ans.append("removeMin")
    
        if not heap or heap[0] > int(x[1]):
            heapq.heappush(heap, int(x[1]))
            ans.append(f"insert {int(x[1])}")
    ans.append(s) 
print(len(ans))
for i in range(len(ans)):
    print(ans[i])