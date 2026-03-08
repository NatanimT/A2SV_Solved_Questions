class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p = 0
        hmap = {0:1}
        cnt = 0
        for i in nums:
            p += i
            g = p - goal
            if g in hmap:
                cnt += hmap[g]
            hmap[p] = hmap.get(p, 0) + 1
        return cnt
            

        