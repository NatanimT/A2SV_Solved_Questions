class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        dire = [(1,0), (-1, 0),(0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        def inbound(i, j):
            return 0<=i< rows and 0<=j<cols
        
        def dfs(r, c,):
            if not inbound(r,c) or board[r][c] != "O":
                return
            board[r][c] ='T'
            for i, j in dire:
                row = r + i
                col = c + j
                dfs(row,col)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i == 0 or i == rows-1 or j == 0 or j == cols-1):
                    dfs(i,j)
                
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X" 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "T":
                    board[i][j] = "O" 
   

        