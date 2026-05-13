class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adjlist = defaultdict(list)
        indegree = [0] * n
        q = deque()
        for f, to in edges:
            adjlist[f].append(to)
            indegree[to] += 1
        ans = [set() for _ in range(n)]
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for nei in adjlist[node]:
                indegree[nei] -= 1
                ans[nei].add(node)
                ans[nei] |= ans[node]
                if indegree[nei] == 0:
                    q.append(nei)
        return [sorted(x) for x in ans]