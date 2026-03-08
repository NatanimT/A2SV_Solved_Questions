class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        p = 0
        ans = 0
        hmap = {0:1}
        for i in nums:
            p += i
            if p % k in hmap:
                ans += hmap[p % k]
            hmap[p % k] = hmap.get(p % k,0) + 1
        return ans

        