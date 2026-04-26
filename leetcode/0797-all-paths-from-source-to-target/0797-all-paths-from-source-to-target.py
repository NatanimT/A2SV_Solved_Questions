class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        t = len(graph) - 1
        path = [0]
        vis = set()
        def dfs(ver):
            if ver == t:
                ans.append(path[:])
                return
            for i in graph[ver]:
                path.append(i)
                dfs(i)
                path.pop()
        dfs(0)
        return ans



        