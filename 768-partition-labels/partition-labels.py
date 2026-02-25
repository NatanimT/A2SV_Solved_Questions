class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = {}
        for i, v in enumerate(s):
            store[v] = i
        ans = []
        start, end = 0,0
        for i, v in enumerate(s):
            end = max(end, store[v])
            if i == end:
                ans.append(end - start + 1)
                start = i + 1
        return ans

