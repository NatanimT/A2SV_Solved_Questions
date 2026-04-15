class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def help(midd):
            cnt = 1 
            prev = position[0]
            for i in position[1:]: 
                if i - prev >= midd:
                    cnt += 1
                    prev = i
                    if cnt >= m:  
                        return True
            return False
        l, r = 1, position[-1] - position[0]
        while l <= r:
            mid = (l + r) // 2
            if help(mid) == True:
                l = mid + 1
            else:
                r = mid - 1
        return r