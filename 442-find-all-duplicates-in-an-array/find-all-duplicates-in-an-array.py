class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = {}
        ans = []
        for i in nums:
            n[i] = n.get(i, 0) + 1
        for x in n:
            if n[x] == 2:
                ans.append(x)
        return ans