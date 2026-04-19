from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums):
        sl = SortedList()
        res = []
        for num in reversed(nums):
            pos = sl.bisect_left(num)
            res.append(pos)
            sl.add(num)
        return res[::-1]
