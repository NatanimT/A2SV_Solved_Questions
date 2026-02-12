class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        h = {}
        res = 0 
        for i in s:
            if (i - 1) not in s:
                length = 0
                while (i + length) in s: 
                    length += 1
                res = max(length, res)
        return res 


            