class Solution(object):
    def predictTheWinner(self, nums):
        def helper(l, r):
            if l == r:
                return nums[l]
            pickL = nums[l] - helper(l + 1, r)
            pickR = nums[r] - helper(l, r - 1)
            return max(pickL, pickR)
        return helper(0, len(nums) - 1) >= 0