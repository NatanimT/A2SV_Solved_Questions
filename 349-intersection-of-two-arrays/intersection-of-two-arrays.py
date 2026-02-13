class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans =[]
        for i in nums1:
            if i in nums2:
                ans.append(i)
        res = list(set(ans))
        return res