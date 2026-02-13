class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        count = Counter(nums)
        n = list(count.keys())
        n.sort(key= lambda x: - count[x])
        for i in range(k):
            ans.append(n[i])
        return ans
