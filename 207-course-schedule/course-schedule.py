class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapp = defaultdict(list)
        for u, v in prerequisites:
            mapp[u].append(v)
        vis = set()
        def dfs(ver):
            if ver in vis:
                return False
            if mapp[ver] == []:
                return True
            vis.add(ver)
            for v in mapp[ver]:
                if not dfs(v):
                    return False
            vis.remove(ver)
            mapp[ver] =[]
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            

            



        