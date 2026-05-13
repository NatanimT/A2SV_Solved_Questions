class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        topsort = defaultdict(list)
        children = defaultdict(list)
        indegree = [0] * n
        q = deque()
        for f, to in edges:
            topsort[f].append(to)
            indegree[to] += 1
            children[to].append(f)
        ans = [set() for _ in range(n)]
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for nei in topsort[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        for node in order:
            for c in children[node]:
                ans[node].add(c)
                for ancestor in ans[c]:
                    ans[node].add(ancestor)
        return [sorted(x) for x in ans]