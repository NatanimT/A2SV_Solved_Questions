class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # changed = [1,3,4,2,6,8] remove 2 , remove 6, remove 8 [1,3,4]
        #            1 1 1 1 1 1
        # [2,6,8,4,12,16]
        #  2,6,8
        if len(changed) % 2 != 0:
            return []
        hashmap = {}
        g1 = []
        
        for i in changed:
            hashmap[i] = hashmap.get(i, 0) + 1
        
        for key in sorted(hashmap.keys()):
            while hashmap[key] > 0:
                if hashmap.get(key * 2, 0) <= 0:
                    return []
                g1.append(key)
                hashmap[key] -= 1  
                hashmap[key * 2] -= 1    
        return g1


        
            