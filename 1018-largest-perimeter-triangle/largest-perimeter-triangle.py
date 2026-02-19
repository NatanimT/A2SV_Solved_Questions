class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = nums
        print(n)
        ans = 0 
        summ = 0
        for i in range(len(n) - 2):
            summ = n[i] + n[i + 1]
            if summ > n[i + 2]:
                ans = (summ + n[i + 2])
        return ans




        