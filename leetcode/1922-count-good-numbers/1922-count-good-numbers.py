class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10**9 + 7
        def power(x, y):
            if y == 0:
                return 1    
            h = power(x, y // 2)
            h = (h * h) % M
            if y % 2:
                return (h * x) % M
            return h
        
        even = (n + 1) // 2
        odd = n // 2    
        return (power(5, even) * power(4, odd)) % M 