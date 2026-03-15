class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        count = Counter(answers)
        for i, v in count.items():
            g = i + 1
            groups = ceil(v / g) 
            ans += g * groups
        return ans


        