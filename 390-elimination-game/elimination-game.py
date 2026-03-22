class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        left = True 
        r = n 
        while r > 1:
            if left or r % 2 == 1:
                head += step  
            step *= 2
            r //= 2
            left = not left
        return head
      
        
