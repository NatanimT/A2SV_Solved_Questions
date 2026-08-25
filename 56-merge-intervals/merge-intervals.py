class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        temp = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if temp[1] >= intervals[i][0]:
                temp = [temp[0], max(temp[1], intervals[i][1])]
            else:
                ans.append(temp)
                temp = intervals[i]
        ans.append(temp)
        return ans

            