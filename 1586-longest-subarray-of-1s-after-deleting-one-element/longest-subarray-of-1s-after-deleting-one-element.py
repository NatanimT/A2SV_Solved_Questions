class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = {}
        res, l = 0, 0
        for r in range(len(nums)):
            cnt[nums[r]] = cnt.get(nums[r], 0) + 1
            while cnt.get(0,0) > 1:
                cnt[nums[l]] -= 1
                l += 1
            res = max(res, r - l)
        return res

        