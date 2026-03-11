class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = [0]

        for i in s:
            if i =="(":
                score.append(0)
            elif score:
                count = score.pop()
                score[-1] += max(1, count * 2)
        return score[-1]



            
