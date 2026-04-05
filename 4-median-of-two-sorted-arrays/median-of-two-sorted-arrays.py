class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = sorted(nums1 + nums2)
        leng = len(m)
        l, r = 0, leng - 1
        mid = (l + r) // 2
        if leng % 2 == 1:
            return m[mid]
        else:
            return (m[mid] + m [mid +1]) / 2


        
        