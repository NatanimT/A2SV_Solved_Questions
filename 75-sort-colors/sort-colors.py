class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0 ,0 ]
        for i in nums:
            count[i] += 1
        r, w, b = count
        nums[:r] = [0] * r
        nums[r:r+w] = [1] * w
        nums[r+w:] = [2] * b
        

        