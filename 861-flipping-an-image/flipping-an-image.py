class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            for j in range(n//2):
                image[i][j],image[i][n-j-1] = image[i][n-j-1],image[i][j]
        print(image)
        for i in range(n):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image