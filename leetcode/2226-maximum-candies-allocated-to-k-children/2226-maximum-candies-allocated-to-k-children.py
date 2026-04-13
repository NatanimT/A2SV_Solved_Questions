class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k :
            return 0
        l, r = 1, max(candies)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            cnt = 0
            for i in candies:
                cnt += i // mid
            if cnt >= k:
                res= max(res, mid)     
                l = mid + 1     
            else:
                r = mid - 1
        return res
            

        