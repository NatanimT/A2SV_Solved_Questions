class Solution:
    def minSteps(self, s: str, t: str) -> int:
      #  cdeeelot acceiprt
        countS = Counter(s) #e:3  d:1 c:1 l:1 o:1 t:1
        countT = Counter(t) #e:1  a:1 i:1 p:1 r:1 t:1
        ans = 0

        for key in countS:
            ans += max(0, countS[key] - countT.get(key,0))
          
        return ans 


                
