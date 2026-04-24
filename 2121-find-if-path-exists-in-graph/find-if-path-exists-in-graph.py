class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mapp = defaultdict(list)
        for u, v in edges:
            mapp[u].append(v)
            mapp[v].append(u)
        s = set([source]) 
        stack = [source]
        while stack:
            x = stack.pop()
            for c in mapp[x]:
                if c not in s:
                    stack.append(c)
                    s.add(c)
        
        if destination in s:
            return True
        return False

        
      

            
        