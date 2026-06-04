class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for n in range(num1, num2 + 1):
            s = str(n)
            length = len(s)
            if length < 3:
                continue
            waviness = 0
            for i in range(1, length - 1):
                left, mid, right = int(s[i-1]), int(s[i]), int(s[i+1])
                if mid > left and mid > right:
                    waviness += 1
                elif mid < left and mid < right:
                    waviness += 1
            total += waviness
        return total