class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        l, r = 0, col * row - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[mid//col][mid%col] :
                return True
            elif target > matrix[mid//col][mid%col]:
                l = mid +1
            else:
                r = mid -1
        return False

        








