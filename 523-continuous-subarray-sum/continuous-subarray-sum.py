class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        mod_map = {0: -1}
        
        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % k
            
            if remainder in mod_map:

                if i - mod_map[remainder] >= 2:
                    return True
            else:
                mod_map[remainder] = i
                
        return False
