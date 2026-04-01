class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:   
        ans = []
        def backtrack(start, comb):
            if len(comb) > 1:
                ans.append(comb[:])   
            used = set()
            for i in range(start, len(nums)):
                if nums[i ] in used:
                    continue
                if not comb or nums[i] >= comb[-1]:
                    used.add(nums[i])
                    comb.append(nums[i])
                    backtrack(i+1, comb)
                    comb.pop()
        backtrack(0, [])
        return ans

        