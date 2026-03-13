class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x : x[0])
        count = 1
        end = points[0][1]
        for x in points[1:]:
            if x[0] > end:
                count += 1
                end = x[1]
            else:
                end = min(end,x[1])
        return count
         
        