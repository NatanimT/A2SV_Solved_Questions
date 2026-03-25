class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def help(start, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return
            for i in range(start, n+ 1):
                comb.append(i)
                help(i+1, comb)

                comb.pop()
        help(1, [])
      
        return ans