class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        d = [(0,1),(0,-1), (1,0), (-1,0)]
        
        s = set()
        def inbound(i, j):
           return 0 <= i< len(grid) and 0<=j < len(grid[0])
        def dfs (s,r,c):
            s.add((r,c))
            p = 0
            for i, j in d:
                nr = r +  i
                nc = c + j
                if not inbound(nr,nc) or grid[nr][nc] == 0:
                    p += 1
                else:
                    if (nr,nc) not in s:
                        p += dfs(s,nr,nc)
            return p
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                   return dfs(s,i,j)




        