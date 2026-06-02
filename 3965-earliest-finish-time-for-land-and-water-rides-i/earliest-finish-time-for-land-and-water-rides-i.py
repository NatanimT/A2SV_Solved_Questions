class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        n = len(landStartTime)
        m = len(waterStartTime)
        for i in range(n):
            for j in range(m):
                l_f = landStartTime[i] + landDuration[i]
                fin1 = max(l_f, waterStartTime[j]) + waterDuration[j]
                w_f = waterStartTime[j] + waterDuration[j]
                fin2 = max(w_f, landStartTime[i]) + landDuration[i]
                ans = min(ans, fin1, fin2)
        return ans
        