class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indeg =[0] * numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for i in adj[node]:
                indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
        if len(ans) == numCourses:
            return ans
        return []



            

        