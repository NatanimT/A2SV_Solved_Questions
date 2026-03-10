class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        ans = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                ans[smaller] = num
            stack.append(num)
        while stack:
            ans[stack.pop()] = -1
                  
        return [ans[num] for num in nums1]
        