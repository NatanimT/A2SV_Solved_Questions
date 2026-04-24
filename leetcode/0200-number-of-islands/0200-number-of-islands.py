class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [(0,1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        def dfs(grid, vis, row, col):
            vis[row][col] = True
            for r, c in d:
                nrow = r + row
                ncol = c + col
                if inbound(nrow, ncol) and not vis[nrow][ncol] and grid[nrow][ncol] == '1':
                    dfs(grid, vis, nrow, ncol)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not vis[i][j]:
                    dfs(grid, vis, i, j)
                    count += 1

        return count 
        

            

