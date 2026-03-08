class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = 0 
        res = float('-inf')
        for i in nums:
            p += i
            res = max(res, p)
            if p < 0:
                p = 0
        return res
            
       



        