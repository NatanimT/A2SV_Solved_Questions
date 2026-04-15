class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums.count(i) > 1:
                ans.append(i)
                break
        for i in range(1, len(nums) + 1):
            if i not in nums:
                ans.append(i)
                break
        return ans

            
        