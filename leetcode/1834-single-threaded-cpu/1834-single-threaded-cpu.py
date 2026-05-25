class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        t = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        t.sort(key=lambda x: x[0])
        res = []
        heap = [] 
        i = 0
        cur_time = 0
        while len(res) < n:
            while i < n and t[i][0] <= cur_time:
                enqueue, p, idx = t[i]
                heapq.heappush(heap, (p, idx))
                i += 1
            if not heap:
                cur_time = t[i][0]
                continue
            p, idx = heapq.heappop(heap)
            res.append(idx)
            cur_time += p
        return res