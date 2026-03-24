class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1:
            return n
        arr = [i for i in range(1, n+1)]
        def help(i,c, arr):
            if len(arr) == 1:
                return arr[0]
            if c == k :
                c = 1
                arr.pop(i)
            return help((i+1) % len(arr), c+1, arr)

        return help(0,1,arr)

