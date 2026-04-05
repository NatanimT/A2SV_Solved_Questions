class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        def help(mid):
            ships, m = 1 , mid
            for i in weights:
                if m - i < 0:
                    ships += 1
                    m = mid
                m -= i
            return ships <= days
        while l <= r:
            mid = (l + r) // 2
            if help(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res

            

        