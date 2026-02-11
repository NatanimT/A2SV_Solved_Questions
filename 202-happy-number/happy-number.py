class Solution:
    def isHappy(self, n: int) -> bool:
        m = list(map(int, str(n)))
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            sqr = 0
            for i in str(n):
                sqr += int(i) *int(i)
            n = sqr

        return True