class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = 0
        for i in range(n + 1):
            expected += i
        summ = sum(nums)
        return expected - summ

        