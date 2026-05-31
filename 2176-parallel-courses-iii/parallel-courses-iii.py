class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for scr, dst in relations:
            adj[scr].append(dst)
        maxT = {}
        def dfs(scr):
            if scr in maxT:
                return maxT[scr]
            res = time[scr-1]
            for nei in adj[scr]:
                res = max(res, time[scr-1] + dfs(nei))
            maxT[scr]= res
            return res
        for i in range(1, n + 1):
            dfs(i)
        return max(maxT.values())
        