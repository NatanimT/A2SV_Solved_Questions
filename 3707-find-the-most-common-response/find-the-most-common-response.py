class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res = []
        ans = []
        for i in responses:
            seen = set()
            group = []
            for x in i:
                if x not in seen:
                    seen.add(x)
                    group.append(x)
            res.append(group)
        result = [word for sub in res for word in sub]
        count = Counter(result)
        max_freq = max(count.values())
        for word in count:
            if count[word] == max_freq:
                ans.append(word)
        ans.sort()
        return ans[0]