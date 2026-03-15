class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        near, far, res =0, 0, 0
        for i in range(len(nums)):
            count[nums[i]] += 1
            
            while len(count) > k:
                count[nums[near]] -= 1
                if count[nums[near]] == 0:
                    count.pop(nums[near])
                near += 1
                far = near
                
            while count[nums[near]] > 1:
                count[nums[near]] -=1
                near += 1
            if len(count) == k:
                res += near - far + 1
                
        return res
        