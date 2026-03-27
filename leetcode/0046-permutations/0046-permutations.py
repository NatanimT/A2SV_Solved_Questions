class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(i, perm):
            if len(perm) == len(nums):
                ans.append(perm[:])
                return 
            for i in nums:
                if i not in perm:
                    perm.append(i)
                    backtrack(i + 1,perm )
                    perm.pop()
        backtrack(0,[])
        return ans