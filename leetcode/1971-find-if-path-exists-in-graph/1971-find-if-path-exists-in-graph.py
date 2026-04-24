class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mapp = defaultdict(list)
        for u, v in edges:
            mapp[u].append(v)
            mapp[v].append(u)
        s = set() 
        def dfs(v, vis):

            vis.add(v)
            for i in mapp[v]:
                if i in vis:
                    continue
                dfs(i, vis)
        dfs(source,s)
        if destination in s:
            return True
        return False

        
      

            
        