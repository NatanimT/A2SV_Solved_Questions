class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []
        p = 1
        for i in range(len(nums)):
            arr.append(p)
            p *= nums[i]

        arr2 = []
        p2 = 1
        for i in range(len(nums)-1,-1, -1):
            arr2.append(p2)
            p2*= nums[i]
        arr2.reverse()

        ans = []
        for i in range(len(nums)):
            ans.append(arr2[i]* arr[i])

        return ans
