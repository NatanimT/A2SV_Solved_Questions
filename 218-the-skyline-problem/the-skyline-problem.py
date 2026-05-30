class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        arr = []
        for l, r, h in buildings:
            arr.append((l, -h))  
            arr.append((r, h))   
        arr.sort()
        result = []
        heap = [0]  
        prev_hei = 0
        remv = {}
        for x, h in arr:
            if h < 0:  
                heapq.heappush(heap, h)
            else:  
                remv[h] = remv.get(h, 0) + 1
            while heap and remv.get(-heap[0], 0) > 0:
                remv[-heap[0]] -= 1
                heapq.heappop(heap)
            curr_hei = -heap[0]
            if curr_hei != prev_hei:
                result.append([x, curr_hei])
                prev_hei = curr_hei
        
        return result