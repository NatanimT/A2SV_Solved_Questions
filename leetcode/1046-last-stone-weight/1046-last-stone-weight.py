class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secStone = heapq.heappop(stones)
            if secStone > firstStone:
                heapq.heappush(stones, firstStone - secStone)
        stones.append(0)
        return abs(stones[0])
        