class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        for i, v in freq.items():
            heap.append([-v, i])
        heapify(heap)
        ans = []
        for _ in range(k):
            freq, word = heappop(heap)
            ans.append(word)
        return ans
        


        