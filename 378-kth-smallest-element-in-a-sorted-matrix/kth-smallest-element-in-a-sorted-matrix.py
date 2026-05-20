class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = flat = [num for row in matrix for num in row]
        heapq.heapify(flat)
        for _ in range(k -1):
            heapq.heappop(flat)
        return heapq.heappop(flat)
