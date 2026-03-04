class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = [0]
        p =0
        for i in range(len(nums)):
            p += nums[i]
            ans.append(p)
        return 1-(min(ans))

        