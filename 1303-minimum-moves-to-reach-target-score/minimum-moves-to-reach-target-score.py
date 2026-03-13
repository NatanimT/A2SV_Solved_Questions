class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n = maxDoubles
        ans = 0
        while target > 1:
            if target % 2 == 0 and n > 0:
                target = target // 2
                n -= 1
                ans += 1        
            elif n == 0:
                ans += target -1
                break
            else:
                target -= 1
                ans +=1           
        return ans

        
            
        

        
        