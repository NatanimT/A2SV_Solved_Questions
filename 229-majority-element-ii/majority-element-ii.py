class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        n = len(nums)
        for i in nums:
            if count[i] > n/3:
                res.append(i)
        ans= list(set(res))
        return ans
