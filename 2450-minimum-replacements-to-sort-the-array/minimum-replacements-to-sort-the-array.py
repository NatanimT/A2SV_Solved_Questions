class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        bigger = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] <= bigger:
                bigger = nums[i]
            else:
                parts = ceil(nums[i] / bigger)
                ans += parts - 1
                bigger = nums[i] // parts
        return ans
            
