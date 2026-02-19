class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        n = len(arr)
        for size in range(n, 1 ,-1):
            maxI = arr.index(size)
            if maxI == size -1:
                continue
            if maxI != 0:

                ans.append(maxI + 1)
                arr[:maxI + 1] = reversed(arr[:maxI + 1])
            ans.append(size)
            arr[:size] = reversed(arr[:size])
        return ans


        