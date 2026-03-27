class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

  
        def help(i, comb):
            if len(comb) == len(digits):
                ans.append(comb)
                return 
            for c in m[digits[i]]:
                help(i + 1, comb + c)

        if digits:
            help(0, "")
        return ans

        