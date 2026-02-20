class Solution:
    def customSortString(self, order: str, s: str) -> str:
        both = []
        only = []
        for i in order:
            for x in s:
                if x == i:
                    both.append(x)
        for j in s:
            if j not in order:
                only.append(j)
        return "". join(both + only)



        