class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        f_lost = {}
        players_set = set()
        res =[]
        l=[]
        w = []
        for x, y in matches:
            players_set.add(x)
            players_set.add(y)
            f_lost[y] = f_lost.get(y, 0) + 1   
        for x in players_set:
            if x not in f_lost:
                w.append(x)
            elif f_lost[x] == 1:
                l.append(x)
        w.sort()
        l.sort()
        res.append(w)
        res.append(l)     
        return res 
        

