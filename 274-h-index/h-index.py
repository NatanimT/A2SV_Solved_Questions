class Solution:
    def hIndex(self, citations: List[int]) -> int:
        val = 0
        n = citations
        for h in range(len(n) + 1):  
            count = 0
            for c in n:
                if c >= h:
                    count += 1       
            if count >= h:
                val = h  
        return val
