class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0: 1}   
        prefix = 0
        count = 0
        
        for num in nums:
            prefix += num
            
            if prefix - k in hmap:
                count += hmap[prefix - k]
            
            hmap[prefix] = hmap.get(prefix, 0) + 1
        
        return count
