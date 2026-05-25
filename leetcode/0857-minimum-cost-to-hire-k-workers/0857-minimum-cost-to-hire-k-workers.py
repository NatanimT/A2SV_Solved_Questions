class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = [] 
        res = float(inf) 
        for i in range(len(quality)):
            pairs.append((wage[i]/ quality[i], quality[i]))
        pairs.sort()
        total_quality = 0
        heap = []
        for r, q in pairs:
            heapq.heappush(heap, -q)
            total_quality += q
            if len(heap) > k:
                total_quality -= -heapq.heappop(heap)
            if len(heap) == k:
                res = min(res, r * total_quality) 
        return res