class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        curr_r = curr_c = 0
        up = True
        res = []
        while len(res) != row * col:
            if up:
                while curr_r >= 0 and curr_c < col:
                    res.append(mat[curr_r][curr_c])
                    curr_r -= 1
                    curr_c += 1
                if curr_c == col:
                    curr_c -= 1
                    curr_r += 2
                else:
                    curr_r += 1
                up = False
            else:
                while curr_r < row and curr_c >= 0:
                    res.append(mat[curr_r][curr_c])
                    curr_c -= 1
                    curr_r += 1
                if curr_r == row:
                    curr_c += 2
                    curr_r -=1
                else:
                    curr_c += 1
                up = True
        return res

        
        